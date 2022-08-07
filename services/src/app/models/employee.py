from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Employee(Base):
    id_employee = Column(
        String(36), ForeignKey("User.id_user"), primary_key=True, index=True
    )
    id_group = Column(
        String(36), ForeignKey("Group.id_group"), primary_key=True, index=True
    )
    id_role = Column(
        String(36), ForeignKey("Role.id_role"), primary_key=True, index=True
    )

    group = relationship("Group", back_populates="employee")
    role = relationship("Role", back_populates="employee")
    user = relationship("User", back_populates="employee")
    contract = relationship("Contract", back_populates="employee")
