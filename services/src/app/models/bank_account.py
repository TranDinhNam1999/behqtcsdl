from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class BankAccount(Base):
    id_bankaccount = Column(
        String(36), ForeignKey("user.id_user"), primary_key=True, index=True
    )
    account_no = Column(String(50), nullable=False)
    account_name = Column(String(100), nullable=False)
    bank_name = Column(String(50), nullable=False)
    bank_branch = Column(String(50), nullable=False)

    driver = relationship("BankAccount", back_populates="bank_account")
