from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Category(Base):
    id_category = Column(String(36), default=uuidv4_str(), primary_key=True, index=True)
    name_category = Column(String(100), nullable=True)

    product = relationship("Product", back_populates="category")
