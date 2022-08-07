from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class HomeAddress(Base):
    id_user = Column(
        String(36), ForeignKey("User.id_user"), primary_key=True, index=True
    )
    city = Column(String(50), nullable=False)
    district = Column(String(50), nullable=False)
    detail = Column(String(256), nullable=True)

    user = relationship("User", back_populates="home_address")
