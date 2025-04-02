from app.auth.db import USERS_DB


def validate_user(username: str, password: str) -> bool:
    if not (db_password := USERS_DB.get(username)):
        return False
    if db_password == password:
        return True
    return False


def create_user(username: str, password: str) -> bool:
    if USERS_DB.get(username):
        return False
    USERS_DB[username] = password
    return True
