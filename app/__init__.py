import redis

from flask import Flask
from flask_jwt_extended import JWTManager

from app import content
from app.auth import auth


def create_app():
    # Create app.
    app = Flask(__name__)

    # Flask App JWT Configuration.
    app.config.from_object("app.config.FlaskSettings")
    app.extensions["jwt"] = JWTManager(app)

    # Redis setup.
    app.extensions["revoked_store"] = redis.StrictRedis(
        host="localhost", port=6379, db=0, decode_responses=True
    )

    # @app.extensions["jwt"].token_in_blocklist_loader
    # def check_if_token_is_revoked(token):
    #     jti = token.get("jti")
    #     entry = app.extensions["revoked_store"].get(jti)
    #
    #     if entry is None:
    #         return True
    #     return entry == "true"

    app.register_blueprint(content.bp)
    app.register_blueprint(auth.bp)
    return app
