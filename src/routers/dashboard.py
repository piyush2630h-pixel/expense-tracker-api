from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.database import get_db
from src.models.user import UserModel
from src.services.dashboard_service import get_dashboard_summary
from src.utils.auth import get_current_user

dashboard_router = APIRouter(prefix="/dashboard",tags=["Dashboard"])

@dashboard_router.get("/")
def dashboard(db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    return get_dashboard_summary(db=db,user_id=current_user.id)