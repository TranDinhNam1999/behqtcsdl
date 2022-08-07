from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Product(Base):
    id_product = Column(String(36), default=uuidv4_str(), primary_key=True, index=True)
    id_branch = Column(String(36), ForeignKey("Branch.id_branch"), index=True)
    id_partner = Column(String(36), ForeignKey("Partner.id_partner"), index=True)
    name_product = Column(String(100), nullable=False)
    describe = Column(Text, nullable=True)
    quality = Column(Integer, server_default=0, nullable=False)
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

    branch = relationship("Branch", back_populates="product")
    partner = relationship("Partner", back_populates="product")
