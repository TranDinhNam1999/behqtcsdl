from datetime import datetime
from typing import Optional
from uuid import uuid4


def uuidv4_str() -> str:
    return str(uuid4())


def current_datetime(fmt: Optional[str] = None) -> Optional[str]:
    if fmt:
        return datetime.utcnow().strftime(fmt)
