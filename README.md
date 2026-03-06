# georgeleeh.com (Flask)

A portfolio/resume Flask app modeled after the structure of your `starmaps-api` project.

## Features

- Flask app factory pattern
- Route module separation (`portfolio/routes`)
- Jinja templates with Bootstrap UI
- Resume, projects, and contact pages
- Docker + Gunicorn support
- Environment-based configuration

## Project structure

- `app.py` – app entry point
- `config.py` – env + content configuration
- `portfolio/__init__.py` – Flask app factory
- `portfolio/routes/main_routes.py` – route handlers
- `portfolio/templates/` – Jinja templates
- `portfolio/static/` – static assets

## Local setup

1. Create env file:
   - `cp .env.example .env`
2. Create virtual env and install:
   - `make init`
   - `make requirements`
3. Run app:
   - `make run`

Open http://127.0.0.1:5000

## Docker

- Build: `make build`
- Run: `make start`
- Stop: `make stop`

## Customize content

Edit the `PROFILE`, `SKILLS`, `EXPERIENCE`, and `PROJECTS` values in `config.py`.
