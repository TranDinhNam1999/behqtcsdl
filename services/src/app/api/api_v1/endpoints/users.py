from typing import Optional, Union

from app import crud
from app.api.deps import get_api_key, get_db, get_trace_id

# from app.core.config import settings
# from app.core.utils import current_datetime
from app.error.base_exception import CustomHTTPException
from app.models.user import User
from app.schemas.user import UserCreate, UserInDB, UserResponse
from fastapi import APIRouter, Depends, status
from fastapi.security.api_key import APIKey
from loguru import logger
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def create_user(
    *,
    user_in: UserCreate,
    db: Session = Depends(get_db),
    api_key: APIKey = Depends(get_api_key),
    trace_id: Union[str, None] = Depends(get_trace_id),
) -> UserResponse:
    """
    Create a user.
    """
    logger.debug(f"incoming request {user_in}")

    user_id_db = crud.user.get_by_id(db=db, id=user_in.id_user)
    user_phone_db = crud.user.get_by_phone(db=db, phone=user_in.phone_number)

    if user_id_db or user_phone_db:
        raise CustomHTTPException(
            code=status.HTTP_406_NOT_ACCEPTABLE, msg="Existing user"
        )

    try:
        user_db: UserInDB = UserInDB(**user_in.dict())

        user_out: Optional[User] = crud.user.create(db=db, obj_in=user_db)
        if not user_out:
            raise CustomHTTPException(
                code=status.HTTP_500_INTERNAL_SERVER_ERROR, msg="Error insert new user"
            )

        logger.debug(f"outgoing response {user_out}")
    except Exception as e:
        logger.warning(e)
        # rollback_user = crud.user.delete(db=db, id=user_in.id_user)

        # if not rollback_user:
        #     raise CustomHTTPException(
        #         code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         msg="Error rollback new user",
        #     )

        raise CustomHTTPException(
            code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            msg="Error insert new user credit",
        )

    user_response: UserInDB = UserInDB(**user_in.dict())
    logger.bind(trace_id=trace_id).success(
        f"Outgoing response /POST user {user_response.dict()}"
    )

    return UserResponse(
        code=status.HTTP_200_OK,
        message="Successful",
        data=user_response,
    )
