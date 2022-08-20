from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class BranchAddress(Base):
    id_branch = Column(
        String(36), ForeignKey("Branch.id_branch"), primary_key=True, index=True
    )
    city = Column(String(50), nullable=False)
    district = Column(String(50), nullable=False)
    detail = Column(String(256), nullable=True)

    branch = relationship("Branch", back_populates="branch_address")
