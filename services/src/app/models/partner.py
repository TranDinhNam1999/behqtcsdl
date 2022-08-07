from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class Partner(Base):
    id_partner = Column(
        String(36), ForeignKey("User.id_user"), primary_key=True, index=True
    )
    representation = Column(String(100), nullable=False)
    number_of_branch = Column(Integer, nullable=False)
    number_order_of_day = Column(Integer, nullable=False)
    product_shipping = Column(Text, nullable=False)
    tax_code = Column(String(50), nullable=False)

    user = relationship("User", back_populates="partner")
    branch = relationship(
        "Branch", back_populates="partner", cascade="all, delete-orphan"
    )
    product = relationship(
        "Product", back_populates="partner", cascade="all, delete-orphan"
    )
    contract = relationship(
        "Contract", back_populates="partner", cascade="all, delete-orphan"
    )
