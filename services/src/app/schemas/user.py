from typing import Optional

import app.core.validators as vls
from pydantic import BaseModel, validator


class UserBase(BaseModel):
    name: str
    dob: str
    email: str
    phone_number: str
    password: str

    @validator("phone_number", pre=True)
    def phone_validator(cls, value):  # noqa: N805
        return vls.phone_validator(value)

    @validator("dob", pre=True)
    def dob_validator(cls, value):  # noqa: N805
        return vls.dob_validator(value)


class UserCreate(UserBase):
    id_user: str
    username: str
    created_date: str
    created_by: str
    is_employee: Optional[int]
    is_driver: Optional[int]
    is_partner: Optional[int]

    @validator("id_user")
    def user_id_validator(cls, value):  # noqa: N805
        return vls.uuid_validator(value)

    @validator("created_date", pre=True)
    def parse_created_at(cls, value):  # noqa: N805
        return vls.datetime_validator(value)

    @validator("created_by")
    def created_by_validator(cls, value):  # noqa: N805
        return vls.uuid_validator(value)


class UserInDB(UserCreate):
    status: Optional[int]

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    modified_date: str
    modified_by: str

    @validator("modified_date", pre=True)
    def parse_created_at(cls, value):  # noqa: N805
        return vls.datetime_validator(value)

    @validator("modified_by")
    def user_id_validator(cls, value):  # noqa: N805
        return vls.uuid_validator(value)


class UserResponse(BaseModel):
    code: int
    message: str
    data: Optional[UserCreate] = None
