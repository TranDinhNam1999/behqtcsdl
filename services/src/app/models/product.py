from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Product(Base):
    id_product = Column(String(36), default=uuidv4_str(), primary_key=True, index=True)
    id_branch = Column(String(36), ForeignKey("Branch.id_branch"), index=True)
    id_partner = Column(String(36), ForeignKey("Partner.id_partner"), index=True)
    id_category = Column(String(36), ForeignKey("Category.id_category"), index=True)
    name_product = Column(String(100), nullable=False)
    describe = Column(Text, nullable=True)
    quality = Column(Integer, default=0, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(Integer, default=1, nullable=False)
    created_date = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        nullable=False,
        index=True,
    )
    created_by = Column(String(36), nullable=True)
    modified_date = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        index=True,
    )
    modified_by = Column(String(36), nullable=True)

    branch = relationship("Branch", back_populates="product")
    partner = relationship("Partner", back_populates="product")
    category = relationship("Category", back_populates="product")
    order_detail = relationship("OrderDetail", back_populates="product")
