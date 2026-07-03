from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import Session
from src.database.database import get_db
from src.schemas.user import UserRegister , UserResponse , UserLogin
from src.services.user_service import create_user , authenticate_user
from src.utils.token import create_access_token
from src.utils.auth import get_current_user
from src.models.user import UserModel

auth_router = APIRouter(prefix = "/auth" , tags = ["Authentication"])

@auth_router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    new_user = create_user(db, user)

    if not new_user:
        raise HTTPException(status_code=400,detail="User with this email already exists...!")

    return new_user

@auth_router.post("/login")
def login_user(user : UserLogin , db : Session = Depends(get_db)):

    authenticated_user = authenticate_user(db,user.email,user.password)

    if not authenticated_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email or password")
    access_token = create_access_token(data={"sub": authenticated_user.email})

    return {"token_type": "bearer" , "access_token": access_token}

@auth_router.get("/me", response_model=UserResponse)
def get_me(current_user: UserModel = Depends(get_current_user)):
    
    return current_user