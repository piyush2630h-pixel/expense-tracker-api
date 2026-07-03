from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database.base import Base


class ExpenseModel(Base):
    __tablename__ = "expense_table"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String(255), nullable=True)
    type = Column(String(20), nullable=False)
    category_id = Column(Integer,ForeignKey("category_table.id"),nullable=False)
    user_id = Column(Integer,ForeignKey("user_table.id"),nullable=False)
    category = relationship("CategoryModel",back_populates="expenses")
    user = relationship("UserModel",back_populates="expenses")