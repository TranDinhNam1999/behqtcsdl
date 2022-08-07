from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Group(Base):
    id_group = Column(String(36), default=uuidv4_str(), primary_key=True, index=True)
    name_group = Column(String(100), nullable=False)

    employee = relationship("Employee", back_populates="group")
