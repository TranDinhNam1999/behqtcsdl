from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class OrderDetail(Base):
    id_order_detail = Column(
        String(36), default=uuidv4_str(), primary_key=True, index=True
    )
    id_order = Column(String(36), ForeignKey("Order.id_order"), index=True)
    id_product = Column(String(36), ForeignKey("Product.id_product"), index=True)
    quality = Column(Integer, default=0, nullable=False)
    price = Column(Float, nullable=False)

    product = relationship("Product", back_populates="order_detail")
    order = relationship("Order", back_populates="order_detail")
