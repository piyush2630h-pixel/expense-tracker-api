from sqlalchemy.orm import Session
from sqlalchemy import func
from src.models.expense import ExpenseModel

def get_dashboard_summary(db: Session, user_id: int):
    total_income = db.query(func.sum(ExpenseModel.amount)).filter(ExpenseModel.user_id == user_id,ExpenseModel.type == "income").scalar() or 0
    total_expense = db.query(func.sum(ExpenseModel.amount)).filter(ExpenseModel.user_id == user_id,ExpenseModel.type == "expense").scalar() or 0
    total_transactions = db.query(ExpenseModel).filter(ExpenseModel.user_id == user_id).count()
    balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "total_transactions": total_transactions
    }