from datetime import timedelta
from pathlib import Path
from environs import Env


BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"
ENV_PATH = BASE_DIR / ".env"


env = Env()
env.read_env(ENV_PATH)


class RedisSettings:
    host = env("REDIS_HOST")
    port = env("REDIS_PORT")
    db = env("REDIS_DB")

    @classmethod
    def get_data(cls):
        return {
            "host": cls.host,
            "port": cls.port,
            "db": cls.db,
        }


class FlaskSettings:
    SECRET_KEY: str = env("FLASK_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES: timedelta = timedelta(minutes=10)
    JWT_TOKEN_LOCATION: list[str] = ["json"]
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
