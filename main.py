from fastapi import FastAPI
from src.models.user import UserModel
from src.routers.auth import auth_router
from src.models.category import CategoryModel
from src.routers.categories import category_router
from src.models.expense import ExpenseModel
from src.routers.expense import expense_router
from src.routers.dashboard import dashboard_router

app = FastAPI(title = "EXPENSE TRACKER API !")
app.include_router(auth_router)
app.include_router(category_router)
app.include_router(expense_router)
app.include_router(dashboard_router)

@app.get("/")
def home():
    return {"msg":"EXPENSE TRACKER API WELCOMES YOU...!"}
