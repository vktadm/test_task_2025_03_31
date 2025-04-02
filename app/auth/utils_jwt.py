from datetime import timedelta

from flask_jwt_extended import create_access_token, get_jti
from app import jwt_redis_blocklist
from app.models import User


def set_jwt_token(user: User) -> dict:
    access_token = create_access_token(identity=user)
    access_token_jti = get_jti(encoded_token=access_token)

    jwt_redis_blocklist.set(access_token_jti, "false", timedelta(minutes=5))
    return dict(access_token=access_token)


def revoked_jwt_token(jti: bytes) -> None:
    jwt_redis_blocklist.set(jti, "true", ex=timedelta(seconds=30))
