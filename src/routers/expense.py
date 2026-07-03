from fastapi import APIRouter, Depends, status , HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.database.database import get_db
from src.models.user import UserModel
from src.schemas.expense import ExpenseCreate, ExpenseResponse
from src.services.expense_service import create_expense , get_user_expenses , update_expense , delete_expense
from src.utils.auth import get_current_user

expense_router = APIRouter(prefix="/expenses",tags=["Expenses"])

@expense_router.post("/",response_model=ExpenseResponse,status_code=status.HTTP_201_CREATED)
def add_expense(expense: ExpenseCreate,db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):

    new_expense = create_expense(db=db,expense=expense,user_id=current_user.id)
    if not new_expense:
        raise HTTPException(status_code=404,detail="Category not found.")

    return new_expense

@expense_router.get("/",response_model=List[ExpenseResponse])
def read_expenses(db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):

    return get_user_expenses(db=db,user_id=current_user.id)

@expense_router.put("/{expense_id}",response_model=ExpenseResponse)
def edit_expense(expense_id: int,expense: ExpenseCreate,db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):

    updated_expense = update_expense(db=db,expense_id=expense_id,expense=expense,user_id=current_user.id)
    if not updated_expense:
        raise HTTPException(status_code=404,detail="Expense or Category not found.")

    return updated_expense

@expense_router.delete("/{expense_id}",status_code=status.HTTP_200_OK)
def remove_expense(expense_id: int,db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):

    deleted_expense = delete_expense(db=db,expense_id=expense_id,user_id=current_user.id)
    if not deleted_expense:
        raise HTTPException(status_code=404,detail="Expense not found.")

    return {"message": "Expense deleted successfully."}