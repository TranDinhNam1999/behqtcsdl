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
    # SQLALCHEMY_DATABASE_URI: str = "mssql+pymssql://<user_name>:<password>@<hostname>:<port>/<db_name>?sslmode=allow"  # noqa: E501
    MSSQL_FREETDS_NAME: str = "<freetds>"
    MSSQL_DATABASE_NAME: str = "<dbname>"
    MSSQL_DATABASE_USER: str = "<username>"
    MSSQL_DATABASE_PASSWORD: str = "<password>"
    SQLALCHEMY_POOL_PRE_PING: int = 1
    SQLALCHEMY_POOL_SIZE: int = 25
    SQLALCHEMY_MAX_OVERFLOW: int = 5
    SQLALCHEMY_POOL_TIMEOUT: int = 45
    SQLALCHEMY_POOL_RECYCLE: int = 3600
    SQLALCHEMY_SESSION_AUTOCOMMIT: int = 0
    SQLALCHEMY_SESSION_AUTOFLUSH: int = 0

    def construct_db_uri(self):
        logger.info(self.MSSQL_FREETDS_NAME)
        logger.info(self.MSSQL_DATABASE_NAME)
        logger.info(self.MSSQL_DATABASE_USER)
        logger.info(self.MSSQL_DATABASE_PASSWORD)
        return f"mssql+pymssql://{self.MSSQL_DATABASE_USER}:{self.MSSQL_DATABASE_PASSWORD}@{self.MSSQL_FREETDS_NAME}/{self.MSSQL_DATABASE_NAME}/?charset=utf8"  # noqa: E501
        # return f"mssql+pyodbc://{self.MSSQL_DATABASE_USER}@{self.MSSQL_DATABASE_HOST}/{self.MSSQL_DATABASE_NAME}?driver=ODBC+Driver+17+for+SQL+Server"  # noqa: E501


class Settings(BaseSettings):
    ENV: str = "DEV"

    API_NAME: str = "Be APIs"
    API_V1_STR: str = "/api/v1"
    API_DOC: str = "openapi.json"
    API_KEY_NAME: str = "Be-Authorization"
    API_KEY_VALUE: str = "xxxx"
    API_TRACE_NAME: str = "X-Trace-Id"

    SUPPORTED_DOB_FORMATS: str = "%Y,%d-%m-%Y,%d/%m/%Y,%d.%m.%Y"

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
        logging_logger.handlers = [InterceptHandler(level=config.logging.LOGGING_LEVEL)]

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
