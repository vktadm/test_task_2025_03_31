from datetime import timedelta
from pathlib import Path
from environs import Env


BASE_DIR = Path(__file__).parent.parent
ENV_PATH = BASE_DIR / ".env"


env = Env()
env.read_env(ENV_PATH)


class FlaskSettings:
    SECRET_KEY: str = env("FLASK_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES: timedelta = timedelta(minutes=5)
    JWT_BLACKLIST_ENABLED: bool = True
    JWT_BLACKLIST_TOKEN_CHECKS: list[str] = ["access"]
    JWT_TOKEN_LOCATION: list[str] = ["json"]
