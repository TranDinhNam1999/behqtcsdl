from app.core.utils import uuidv4_str
from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class BankAccount(Base):
    id_bank_account = Column(
        String(36), default=uuidv4_str(), primary_key=True, index=True
    )
    id_driver = Column(
        String(36), ForeignKey("Driver.id_driver"), primary_key=True, index=True
    )
    account_no = Column(String(50), nullable=False)
    account_name = Column(String(100), nullable=False)
    bank_name = Column(String(50), nullable=False)
    bank_branch = Column(String(50), nullable=False)

    driver = relationship("Driver", back_populates="bank_account")
