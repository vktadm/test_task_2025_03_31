from sqlalchemy.orm import mapped_column, Mapped

from app import db
from enum import Enum


class Role(Enum):
    ADMIN = "admin"
    USER = "user"


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    role: Mapped[Role] = mapped_column(default=Role.USER)

    def __repr__(self):
        return f"<User {self.username}>"
