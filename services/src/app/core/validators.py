import uuid
from datetime import datetime


def uuid_validator(value):
    if value:
        try:
            uuid.UUID(value)
        except ValueError as e:
            raise e
    return value


def phone_validator(value):
    if not value:
        raise ValueError("Can't be null")
    if not isinstance(value, str):
        raise ValueError("Error type, must be str")
    if len(value) < 12 or len(value) > 14:
        raise ValueError("Length must be between 12 and 14")
    return value


def dob_validator(value):
    if value:
        if not isinstance(value, str):
            raise ValueError("Error type, must be str")
        return value


def datetime_validator(value, fmt="%Y-%m-%dT%H:%M:%S.%f%z"):
    if value:
        try:
            if isinstance(value, str):
                return datetime.strptime(value, fmt)
            if isinstance(value, datetime):
                return value
        except ValueError as e:
            raise e
