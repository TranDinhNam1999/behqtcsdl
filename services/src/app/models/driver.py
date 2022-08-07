from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Driver(Base):
    id_driver = Column(
        String(36), ForeignKey("user.id_user"), primary_key=True, index=True
    )
    id_bankaccount = Column(String(36), ForeignKey("user.id_user"), index=True)
    id_card = Column(String(50), nullable=False)
    license_plates = Column(String(50), nullable=False)
    working_city = Column(String(50), nullable=False)
    working_district = Column(String(50), nullable=False)

    bank_account = relationship(
        "Driver", back_populates="driver", cascade="all, delete-orphan"
    )
    user = relationship("Driver", back_populates="driver")
