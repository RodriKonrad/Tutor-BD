from flask import Flask


def create_app(config_object=None):
    """Application factory for the Flask app."""
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # Load config
    if config_object:
        app.config.from_object(config_object)
    else:
        app.config.from_mapping(
            SECRET_KEY="dev",
        )

    # Register blueprints
    from .main import main as main_bp
    from .auth import auth as auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
