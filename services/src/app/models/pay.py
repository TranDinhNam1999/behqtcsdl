from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Pay(Base):
    id_pay = Column(String(36), default=uuidv4_str(), primary_key=True, index=True)
    name_pay = Column(String(100), nullable=False)

    order = relationship("Order", back_populates="pay")
