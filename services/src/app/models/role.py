from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Role(Base):
    id_role = Column(String(36), default=uuidv4_str(), primary_key=True, index=True)
    name_role = Column(String(100), nullable=True)
    can_edit_data = Column(Integer, default=0, nullable=False)
    can_edit_user = Column(Integer, default=0, nullable=False)
    can_manage_ui = Column(Integer, default=0, nullable=False)

    employee = relationship("Employee", back_populates="role")
