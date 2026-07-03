from sqlalchemy.orm import Session
from src.models.expense import ExpenseModel
from src.models.category import CategoryModel

def create_expense(db: Session,expense,user_id: int):
    category = db.query(CategoryModel).filter(CategoryModel.id == expense.category_id,CategoryModel.user_id == user_id).first()

    if not category:
        return None

    new_expense = ExpenseModel(
        title=expense.title,
        amount=expense.amount,
        description=expense.description,
        type=expense.type,
        category_id=expense.category_id,
        user_id=user_id
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense

def get_user_expenses(db: Session, user_id: int):
    return db.query(ExpenseModel).filter(ExpenseModel.user_id == user_id).all()

def update_expense(db: Session,expense_id: int,expense,user_id: int):
    existing_expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id,ExpenseModel.user_id == user_id).first()
    if not existing_expense:
        return None

    category = db.query(CategoryModel).filter(CategoryModel.id == expense.category_id,CategoryModel.user_id == user_id).first()
    if not category:
        return None

    existing_expense.title = expense.title
    existing_expense.amount = expense.amount
    existing_expense.description = expense.description
    existing_expense.type = expense.type
    existing_expense.category_id = expense.category_id

    db.commit()
    db.refresh(existing_expense)

    return existing_expense

def delete_expense(db: Session,expense_id: int,user_id: int):
    expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id,ExpenseModel.user_id == user_id).first()

    if not expense:
        return None

    db.delete(expense)
    db.commit()

    return expense