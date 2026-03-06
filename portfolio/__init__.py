"""Flask application factory for the portfolio site."""

import logging
from datetime import datetime, timezone

from flask import Flask
from flask_cors import CORS

from config import Config
from .analytics import init_analytics_db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    init_analytics_db(app)

    if not app.logger.handlers:
        logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(logging.INFO)

    from .routes.main_routes import main_bp

    app.register_blueprint(main_bp)

    @app.context_processor
    def inject_globals():
        analytics_key = (app.config.get("ANALYTICS_DASHBOARD_KEY") or "").strip()
        return {
            "site_title": app.config["SITE_TITLE"],
            "contact_email": app.config["CONTACT_EMAIL"],
            "linkedin_url": app.config["LINKEDIN_URL"],
            "analytics_public": not bool(analytics_key),
            "current_year": datetime.now(timezone.utc).year,
        }

    return app
