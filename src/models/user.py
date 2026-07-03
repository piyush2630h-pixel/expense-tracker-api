from sqlalchemy import Column , Integer , String , Boolean
from src.database.base import Base
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = "user_table"

    id = Column(Integer , primary_key = True , index = True)
    username = Column(String(100) , nullable = False)
    email = Column(String(255) , nullable = False)
    password = Column(String(255) , nullable = False)

    categories = relationship(
    "CategoryModel",
    back_populates="user",
    cascade="all, delete-orphan"
    )

    expenses = relationship(
        "ExpenseModel",
        back_populates="user",
        cascade="all, delete-orphan"
    )