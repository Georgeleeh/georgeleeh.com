"""Flask application factory for the portfolio site."""

import logging
from datetime import datetime, timezone

from flask import Flask
from flask_cors import CORS

from config import Config


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    if not app.logger.handlers:
        logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(logging.INFO)

    from .routes.main_routes import main_bp

    app.register_blueprint(main_bp)

    @app.context_processor
    def inject_globals():
        return {
            "site_title": app.config["SITE_TITLE"],
            "contact_email": app.config["CONTACT_EMAIL"],
            "github_url": app.config["GITHUB_URL"],
            "linkedin_url": app.config["LINKEDIN_URL"],
            "current_year": datetime.now(timezone.utc).year,
        }

    return app
