from fastapi import APIRouter, Depends, status , HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.database.database import get_db
from src.models.user import UserModel
from src.schemas.category import CategoryCreate, CategoryResponse
from src.services.category_service import create_category , get_user_categories , update_category , delete_category
from src.utils.auth import get_current_user

category_router = APIRouter(prefix="/categories",tags=["Categories"])

@category_router.post("/",response_model=CategoryResponse,status_code=status.HTTP_201_CREATED)
def add_category(category: CategoryCreate,db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    new_category = create_category(db=db,name=category.name,user_id=current_user.id)
    
    if not new_category:
        raise HTTPException(status_code=400,detail="Category already exists.")

    return new_category

@category_router.get("/",response_model=List[CategoryResponse])
def read_categories(db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    
    return get_user_categories(db=db,user_id=current_user.id)

@category_router.put("/{category_id}",response_model=CategoryResponse)
def edit_category(category_id: int,category: CategoryCreate,db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):

    updated_category = update_category(
        db=db,
        category_id=category_id,
        name=category.name,
        user_id=current_user.id
        )

    if not updated_category:
        raise HTTPException(status_code=404,detail="Category not found.")

    return updated_category

@category_router.delete("/{category_id}",status_code=status.HTTP_200_OK)
def remove_category(category_id: int,db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    
    deleted_category = delete_category(
        db=db,
        category_id=category_id,
        user_id=current_user.id
    )

    if not deleted_category:
        raise HTTPException(status_code=404,detail="Category not found.")

    return {"message": "Category deleted successfully."}