"""Модуль для работы с БД"""

from app.auth.en_de_cryption import hash_password, validate_password
from app.models import User, Role
from app import db


def gey_user_by_username(username: str) -> User | None:
    return db.session.query(User).filter_by(username=username).scalar()


def validate_user(username: str, password: str) -> User | None:
    user = gey_user_by_username(username)
    if user and validate_password(password, user.password):
        return user
    return None


def create_user(username: str, password: str, role: str | None) -> User | None:
    user = gey_user_by_username(username)
    if user:
        return None
    new_user = User(
        username=username,
        password=hash_password(password),
        role=Role.ADMIN if Role.ADMIN.value == role else Role.USER,
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user
