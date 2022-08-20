from typing import Any, Dict, Optional, Union

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserInDB, UserUpdate
from loguru import logger
from sqlalchemy.orm import Session


class CRUDUser(CRUDBase[User, UserInDB, UserUpdate]):
    def get_by_id(self, db: Session, *, id: str) -> Optional[User]:
        return db.query(User).filter(User.id_user == id).first()

    def get_by_phone(self, db: Session, *, phone: str) -> Optional[User]:
        return db.query(User).filter(User.phone_number == phone).first()

    def create(self, db: Session, *, obj_in: UserInDB) -> Optional[User]:
        try:
            create_data = obj_in.dict()
            db_obj = User(**create_data)
            db.add(db_obj)
            db.commit()
        except Exception as e:
            logger.warning(e)
            db.rollback()
        else:
            return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> Optional[User]:
        try:
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.dict(exclude_unset=True)

            update_user = super().update(db, db_obj=db_obj, obj_in=update_data)

        except Exception as e:
            logger.warning(e)
            db.rollback()
        else:
            return update_user

    def delete(self, db: Session, *, id: str) -> Optional[User]:
        try:
            obj = db.query(User).get(id)
            db.delete(obj)
            db.commit()
        except Exception as e:
            logger.warning(e)
            db.rollback()
        else:
            return obj


user = CRUDUser(User)
