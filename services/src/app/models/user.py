from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class User(Base):
    id_user = Column(String(36), default=uuidv4_str(), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(36), nullable=False)
    phone_number = Column(String(18), index=True, nullable=False)
    dob = Column(String(10), nullable=True)
    email = Column(String(100), nullable=True)
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
    is_employee = Column(Integer, default=0, nullable=False)
    is_driver = Column(Integer, default=0, nullable=False)
    is_partner = Column(Integer, default=0, nullable=False)
    status = Column(Integer, default=1, nullable=False)

    order = relationship("Order", back_populates="user", cascade="all, delete-orphan")
    driver = relationship("Driver", back_populates="user", cascade="all, delete-orphan")
    employee = relationship(
        "Employee", back_populates="user", cascade="all, delete-orphan"
    )
    partner = relationship(
        "Partner", back_populates="user", cascade="all, delete-orphan"
    )
    home_address = relationship(
        "HomeAddress", back_populates="user", cascade="all, delete-orphan"
    )
    delivery_address = relationship(
        "DeliveryAddress", back_populates="user", cascade="all, delete-orphan"
    )
