from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify

import jwt

from app.config import settings


def encode_jwt(
    payload: dict,
    key: str = settings.secret,
    algorithm: str = settings.algorithm,
    expire_minutes: int = settings.access_token_expire_minutes,
):
    to_encode = payload.copy()
    now = datetime.utcnow()
    expire = now + timedelta(minutes=expire_minutes)

    to_encode.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(to_encode, key, algorithm=algorithm)

    return encoded


def decode_jwt(
    token: str | bytes,
    key: str = settings.secret,
    algorithms: str = settings.algorithm,
):
    decoded = jwt.decode(
        jwt=token,
        key=key,
        algorithms=algorithms,
    )
    return decoded


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.json.get("token")
        if not token:
            return jsonify({"Alert!": "Token is missing"}), 401
        try:
            payload = decode_jwt(token=token)
        except jwt.ExpiredSignatureError:
            return jsonify({"Alert!": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"Alert!": "Invalid Token"}), 401

        return func(*args, **kwargs)  # Correctly return the wrapped function

    return decorated
