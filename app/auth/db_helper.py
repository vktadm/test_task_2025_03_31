import bcrypt
from flask import abort

from app.redis_client import get_redis_client
from app.auth import utils_jwt


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(
        pwd_bytes,
        salt,
    )


def validate_password(
    password: str,
    hashed_password: bytes,
) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password,
    )


def validate_user(username: str, password: str):
    redis_client = get_redis_client()

    if not (hashed_password := redis_client.get(username)):
        abort(401, "Invalid username")

    # if utils_jwt.validate_password(password=password, hashed_password=hashed_password):
    if password == hashed_password.decode("utf-8"):
        return username

    abort(401, "Invalid password")
