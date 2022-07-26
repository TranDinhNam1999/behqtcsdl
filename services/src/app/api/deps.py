from typing import Generator

from app.core.config import settings
from app.db.session import SessionLocal
from app.error.base_exception import CustomHTTPException
from fastapi import Security, status
from fastapi.security.api_key import APIKeyHeader
from loguru import logger

_api_key_header = APIKeyHeader(name=settings.API_KEY_NAME, auto_error=False)


async def get_api_key(api_key_header: str = Security(_api_key_header)):
    if api_key_header == settings.API_KEY_VALUE:
        return api_key_header
    else:
        logger.warning("wrong api key")
        raise CustomHTTPException(
            code=status.HTTP_401_UNAUTHORIZED, msg="Wrong api key"
        )


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
