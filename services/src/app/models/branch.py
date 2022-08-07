from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Branch(Base):
    id_branch = Column(String(36), default=uuidv4_str(), primary_key=True, index=True)
    id_partner = Column(String(36), ForeignKey("Partner.id_partner"), index=True)
    name_branch = Column(String(100), nullable=True)
    created_date = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        nullable=False,
        index=True,
    )
    create_by = Column(String(36), nullable=True)
    modified_date = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        index=True,
    )
    modified_by = Column(String(36), nullable=True)
    is_deleted = Column(Integer, server_default=0, nullable=False)

    branch_address = relationship("BranchAddress", back_populates="branch")
    partner = relationship("Partner", back_populates="branch")
    product = relationship("Product", back_populates="branch")
