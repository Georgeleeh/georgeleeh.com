"""Lightweight first-party analytics helpers."""

from __future__ import annotations

import hashlib
import json
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from flask import Flask


def _db_path(app: Flask) -> Path:
    configured = app.config.get("ANALYTICS_DB_PATH")
    if configured:
        return Path(configured)
    return Path(app.instance_path) / "analytics.db"


def init_analytics_db(app: Flask) -> None:
    db_path = _db_path(app)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS analytics_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                event_type TEXT NOT NULL,
                path TEXT,
                referrer TEXT,
                visitor_id TEXT,
                session_id TEXT,
                metadata TEXT,
                user_agent TEXT,
                ip_hash TEXT
            )
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_analytics_created_at
            ON analytics_events(created_at)
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_analytics_event_type
            ON analytics_events(event_type)
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_analytics_path
            ON analytics_events(path)
            """
        )


def _connect(app: Flask) -> sqlite3.Connection:
    conn = sqlite3.connect(_db_path(app))
    conn.row_factory = sqlite3.Row
    return conn


def _hash_ip(ip_address: str | None) -> str | None:
    if not ip_address:
        return None
    return hashlib.sha256(ip_address.encode("utf-8")).hexdigest()[:16]


def track_event(
    app: Flask,
    *,
    event_type: str,
    path: str | None,
    referrer: str | None,
    visitor_id: str | None,
    session_id: str | None,
    metadata: dict[str, Any] | None,
    user_agent: str | None,
    ip_address: str | None,
) -> None:
    safe_event_type = (event_type or "unknown")[:64]
    safe_path = (path or "")[:255] or None
    safe_referrer = (referrer or "")[:500] or None
    safe_visitor = (visitor_id or "")[:128] or None
    safe_session = (session_id or "")[:128] or None
    safe_metadata = json.dumps(metadata or {}, ensure_ascii=False)[:2000]
    safe_user_agent = (user_agent or "")[:500] or None

    if safe_path and safe_path.startswith("/analytics"):
        return

    with _connect(app) as conn:
        conn.execute(
            """
            INSERT INTO analytics_events (
                created_at,
                event_type,
                path,
                referrer,
                visitor_id,
                session_id,
                metadata,
                user_agent,
                ip_hash
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.now(timezone.utc).isoformat(),
                safe_event_type,
                safe_path,
                safe_referrer,
                safe_visitor,
                safe_session,
                safe_metadata,
                safe_user_agent,
                _hash_ip(ip_address),
            ),
        )


def get_metrics(app: Flask, *, days: int = 30) -> dict[str, Any]:
    days = max(1, min(days, 180))
    since = datetime.now(timezone.utc) - timedelta(days=days)
    since_iso = since.isoformat()

    with _connect(app) as conn:
        totals_row = conn.execute(
            """
            SELECT
                COUNT(*) AS total_events,
                SUM(CASE WHEN event_type = 'page_view' THEN 1 ELSE 0 END) AS page_views,
                COUNT(DISTINCT CASE
                    WHEN visitor_id IS NOT NULL AND visitor_id != '' THEN visitor_id
                    ELSE ip_hash
                END) AS unique_visitors,
                COUNT(DISTINCT session_id) AS sessions
            FROM analytics_events
            WHERE created_at >= ?
                            AND (path IS NULL OR path NOT LIKE '/analytics%')
            """,
            (since_iso,),
        ).fetchone()

        top_pages = conn.execute(
            """
            SELECT path, COUNT(*) AS views
            FROM analytics_events
            WHERE created_at >= ?
              AND event_type = 'page_view'
              AND path IS NOT NULL
              AND path != ''
                            AND path NOT LIKE '/analytics%'
            GROUP BY path
            ORDER BY views DESC
            LIMIT 10
            """,
            (since_iso,),
        ).fetchall()

        engagement = conn.execute(
            """
            SELECT event_type, COUNT(*) AS count
            FROM analytics_events
            WHERE created_at >= ?
              AND event_type != 'page_view'
                            AND (path IS NULL OR path NOT LIKE '/analytics%')
            GROUP BY event_type
            ORDER BY count DESC
            LIMIT 12
            """,
            (since_iso,),
        ).fetchall()

        daily_views = conn.execute(
            """
            SELECT substr(created_at, 1, 10) AS day, COUNT(*) AS views
            FROM analytics_events
            WHERE created_at >= ?
              AND event_type = 'page_view'
                            AND (path IS NULL OR path NOT LIKE '/analytics%')
            GROUP BY day
            ORDER BY day ASC
            """,
            (since_iso,),
        ).fetchall()

        recent_events = conn.execute(
            """
            SELECT created_at, event_type, path
            FROM analytics_events
            WHERE path IS NULL OR path NOT LIKE '/analytics%'
            ORDER BY id DESC
            LIMIT 20
            """
        ).fetchall()

    totals = {
        "total_events": int(totals_row["total_events"] or 0),
        "page_views": int(totals_row["page_views"] or 0),
        "unique_visitors": int(totals_row["unique_visitors"] or 0),
        "sessions": int(totals_row["sessions"] or 0),
    }

    return {
        "days": days,
        "totals": totals,
        "top_pages": [dict(row) for row in top_pages],
        "engagement": [dict(row) for row in engagement],
        "daily_views": [dict(row) for row in daily_views],
        "recent_events": [dict(row) for row in recent_events],
    }
