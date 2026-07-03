from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database.base import Base


class CategoryModel(Base):
    __tablename__ = "category_table"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    user_id = Column(
        Integer,
        ForeignKey("user_table.id"),
        nullable=False
    )

    user = relationship(
        "UserModel",
        back_populates="categories"
    )

    expenses = relationship(
    "ExpenseModel",
    back_populates="category",
    cascade="all, delete-orphan"
    )