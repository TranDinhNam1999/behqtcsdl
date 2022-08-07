from typing import Generator, Union

from app.core.config import settings
from app.db.session import SessionLocal
from app.error.base_exception import CustomHTTPException
from fastapi import Header, Security, status
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


async def get_trace_id(
    x_trace_id: Union[str, None] = Header(default=None, title=settings.API_TRACE_NAME)
) -> Union[str, None]:
    logger.warning(f"detected {x_trace_id} in header")
    if x_trace_id is not None:
        return x_trace_id

    logger.warning(f"not detected {settings.API_TRACE_NAME} in header")
    return None


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
