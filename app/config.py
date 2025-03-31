import logging
from pathlib import Path
from environs import Env


BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"
ENV_PATH = BASE_DIR / ".env"


env = Env()
env.read_env(ENV_PATH)


class DBSettings:
    url: str = f"sqlite:////{DB_PATH}"
    echo: bool = True  # TODO: отладка


class Settings:
    secret: str = env("FLASK_SECRET_KEY")
    redis_url: str = (
        f"redis://{env("REDIS_HOST")}:{env("REDIS_PORT")}/{env("REDIS_DB")}"
    )
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 3


settings = Settings()
