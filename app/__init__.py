from flask import Flask
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    from app.api.horoscope.routes import horoscope_bp
    from app.api.search.routes import search_bp

    app.register_blueprint(horoscope_bp)
    app.register_blueprint(search_bp)

    return app