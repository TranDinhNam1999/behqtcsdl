from app.error.base_exception import CustomHTTPException
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from loguru import logger
from sqlalchemy.exc import DatabaseError, DataError, IntegrityError


def add_app_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exception: Exception):

        exception_str = exception.args
        logger.error(exception)

        return CustomHTTPException(
            code=status.HTTP_500_INTERNAL_SERVER_ERROR, msg=str(exception_str)
        ).to_json()

    @app.exception_handler(DatabaseError)
    async def db_connection_exception_handler(
        request: Request, exception: DatabaseError
    ):

        exception_str = exception.args
        logger.warning(exception)

        return CustomHTTPException(
            code=status.HTTP_503_SERVICE_UNAVAILABLE, msg=str(exception_str)
        ).to_json()

    @app.exception_handler(DataError)
    async def db_validator_exception_handler(request: Request, exception: DataError):

        exception_str = exception.args
        logger.warning(exception)

        return CustomHTTPException(
            code=status.HTTP_400_BAD_REQUEST, msg=str(exception_str)
        ).to_json()

    @app.exception_handler(IntegrityError)
    async def db_contraint_exception_handler(
        request: Request, exception: IntegrityError
    ):

        exception_str = exception.args
        logger.warning(exception_str)

        return CustomHTTPException(
            code=status.HTTP_400_BAD_REQUEST, msg=str(exception_str)
        ).to_json()

    @app.exception_handler(RequestValidationError)
    async def general_http_exception_handler(
        request: Request, exception: RequestValidationError
    ):
        exception_str = str(exception)
        logger.warning(exception_str)

        return CustomHTTPException(
            code=status.HTTP_400_BAD_REQUEST, msg=exception_str
        ).to_json()

    @app.exception_handler(CustomHTTPException)
    async def custom_http_exception_handler(
        request: Request, exception: CustomHTTPException
    ):
        return exception.to_json()
