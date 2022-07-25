import logging
import sys

from app.core import logging as lg
from app.core.logging import InterceptHandler
from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseSettings

load_dotenv()


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.DEBUG
    LOGGERS: tuple = ("uvicorn.asgi", "uvicorn.access", "fastapi")
    LOGGING_ENQUEUE: bool = True
    LOGGING_BACKTRACE: bool = True


class DBSettings(BaseSettings):
    # SQLALCHEMY_DATABASE_URI: str = "postgresql://<user_name>:<password>@<hostname>:5432/<db_name>?sslmode=allow"  # noqa: E501
    POSTGRES_DATABASE_HOST: str = (
        "<hostname>:5432"
    )
    POSTGRES_DATABASE_NAME: str = ""
    POSTGRES_DATABASE_USER: str = ""
    POSTGRES_DATABASE_PASSWORD: str = ""
    SQLALCHEMY_POOL_PRE_PING: int = 1
    SQLALCHEMY_POOL_SIZE: int = 25
    SQLALCHEMY_MAX_OVERFLOW: int = 5
    SQLALCHEMY_POOL_TIMEOUT: int = 45
    SQLALCHEMY_POOL_RECYCLE: int = 3600
    SQLALCHEMY_SESSION_AUTOCOMMIT: int = 0
    SQLALCHEMY_SESSION_AUTOFLUSH: int = 0

    def construct_db_uri(self):
        return f"postgresql://{self.POSTGRES_DATABASE_USER}:{self.POSTGRES_DATABASE_PASSWORD}@{self.POSTGRES_DATABASE_HOST}/{self.POSTGRES_DATABASE_NAME}?sslmode=allow"  # noqa: E501


class Settings(BaseSettings):
    ENV: str = "DEV"

    API_NAME: str = "User API"
    API_V1_STR: str = "/api/v1"
    API_DOC: str = "openapi.json"
    API_KEY_NAME: str = ""
    API_KEY_VALUE: str = ""
    API_KEY_UNIQUE_VALUE: str = ""
    API_TRACE_NAME: str = ""

    db: DBSettings = DBSettings()
    logging: LoggingSettings = LoggingSettings()

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


def setup_app_logging(config: Settings) -> None:
    logging.getLogger().handlers = [InterceptHandler()]
    for logger_name in config.logging.LOGGERS:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(
            level=config.logging.LOGGING_LEVEL)]

    logger.configure(
        handlers=[
            {
                "sink": sys.stderr,
                "enqueue": config.logging.LOGGING_ENQUEUE,
                "backtrace": config.logging.LOGGING_BACKTRACE,
                "level": config.logging.LOGGING_LEVEL,
                "format": lg.format_record_development,
            }
        ]
    )


settings = Settings()
