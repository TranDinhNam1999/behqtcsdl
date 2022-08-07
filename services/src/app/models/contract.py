from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Contract(Base):
    id_contract = Column(String(36), default=uuidv4_str(), primary_key=True, index=True)
    id_employee = Column(String(36), ForeignKey("User.id_employee"), index=True)
    id_partner = Column(String(36), ForeignKey("Partner.id_partner"), index=True)
    tax_code_partner = Column(String(50), nullable=False)
    representation = Column(String(100), nullable=False)
    number_of_registered_branch = Column(Integer, default=0, nullable=False)
    effective_time = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        index=True,
    )
    commission_percentage = Column(Numeric, nullable=False)
    activation_fee = Column(Numeric, nullable=False)
    status = Column(Integer, default=0, nullable=False)
    created_date = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        nullable=False,
        index=True,
    )
    create_by = Column(String(36), nullable=True)

    employee = relationship("Employee", back_populates="contract")
    partner = relationship("Partner", back_populates="contract")
