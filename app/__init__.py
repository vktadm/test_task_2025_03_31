import redis

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

jwt = JWTManager()

# Redis blocklist.
jwt_redis_blocklist = redis.StrictRedis(
    host="172.17.0.2", port=8080, db=0, decode_responses=True
)


def create_app():
    # Create app.
    app = Flask(__name__)

    # Flask App and JWT configuration.
    app.config.from_object("app.config.FlaskSettings")
    jwt.init_app(app)

    # DB init.
    db.init_app(app)

    from app.models import User

    with app.app_context():
        db.create_all()

    # Callback function to check if a JWT exists in the redis blocklist.
    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
        jti = jwt_payload["jti"]
        token_in_redis = jwt_redis_blocklist.get(jti)
        if token_in_redis in [None, "true"]:
            return True
        return False

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return str(user.id)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = int(jwt_data["sub"])
        return User.query.filter_by(id=identity).one_or_none()

    from app import content
    from app.auth import auth

    app.register_blueprint(content.bp)
    app.register_blueprint(auth.bp)

    return app
