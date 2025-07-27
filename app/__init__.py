from flask import Flask
from .extensions import db
from .config import Config


def create_app():
    # Application factory function
    app = Flask(__name__)

    app.config.from_object(Config)

    initialize_extensions(app)

    register_blueprints(app)

    setup_database(app)

    register_commands(app)

    return app


def initialize_extensions(app):
    # Initialize Flask extensions
    db.init_app(app)


def register_blueprints(app):
    # Register Flask blueprints
    from .api.horoscope.routes import horoscope_bp
    from .api.search.routes import search_bp
    from .api.favorites.routes import favorites_bp

    app.register_blueprint(horoscope_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(favorites_bp)


def setup_database(app):
    # Setup database and create tables
    with app.app_context():
        try:
            db.create_all()
            app.logger.info("Database tables created successfully")
        except Exception as e:
            app.logger.error(f"Failed to create database tables: {str(e)}")
            raise


def register_commands(app):
    @app.cli.command("init-db")
    def init_db():
        # Initialize the database
        with app.app_context():
            try:
                db.create_all()
                print("Database tables created successfully")
            except Exception as e:
                print(f"Error creating database tables: {str(e)}")
                raise