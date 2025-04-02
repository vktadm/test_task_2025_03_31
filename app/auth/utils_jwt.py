from datetime import timedelta

from flask_jwt_extended import (
    create_access_token,
    get_jti,
    get_jwt,
)
from flask import current_app


def set_jwt_token(username: str) -> dict:
    access_token = create_access_token(identity=username)
    access_token_jti = get_jti(encoded_token=access_token)
    current_app.extensions["revoked_store"].set(
        access_token_jti, "false", timedelta(minutes=1)
    )
    return dict(access_token=access_token)


def revoked_jwt_token(jti):
    current_app.extensions["revoked_store"].set(jti, "true", timedelta(seconds=5))
