from flask import Flask
from app.config import settings


def create_app():
    # Create and configure the app.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=settings.secret,
        REDIS_URL=settings.redis_url,
    )

    from app import content

    from app.auth import auth

    app.register_blueprint(content.bp)
    app.register_blueprint(auth.bp)

    return app
