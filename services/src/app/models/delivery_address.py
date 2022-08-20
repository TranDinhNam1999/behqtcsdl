from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class DeliveryAddress(Base):
    id_delivery_address = Column(
        String(36), default=uuidv4_str(), primary_key=True, index=True
    )
    id_user = Column(String(36), ForeignKey("User.id_user"), index=True)
    city = Column(String(50), nullable=False)
    district = Column(String(50), nullable=False)
    detail = Column(String(256), nullable=True)

    user = relationship("User", back_populates="delivery_address")
    order = relationship("Order", back_populates="delivery_address")
