from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Order(Base):
    id_order = Column(String(36), default=uuidv4_str(), primary_key=True, index=True)
    id_partner = Column(String(36), ForeignKey("Partner.id_partner"), index=True)
    id_pay = Column(String(36), ForeignKey("Pay.id_pay"), index=True)
    id_buyer = Column(String(36), ForeignKey("User.id_user"), index=True)
    id_delivery_address = Column(
        String(36), ForeignKey("DeliveryAddress.id_delivery_address"), index=True
    )
    status_order = Column(Integer, default=0, nullable=False)
    cost_order = Column(Float, nullable=False)
    cost_transport = Column(Float, nullable=False)
    sumcost = Column(Float, nullable=False)
    is_handler = Column(Integer, default=0, nullable=False)
    created_date = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        nullable=False,
        index=True,
    )
    modified_date = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        index=True,
    )

    user = relationship("User", back_populates="order")
    delivery_address = relationship("DeliveryAddress", back_populates="order")
    partner = relationship("Partner", back_populates="order")
    pay = relationship("Pay", back_populates="order")
    order_detail = relationship("OrderDetail", back_populates="order")
