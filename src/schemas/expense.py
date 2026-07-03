from pydantic import BaseModel, Field

class ExpenseCreate(BaseModel):
    title: str = Field(..., min_length=2, max_length=100)
    amount: float = Field(..., gt=0)
    description: str | None = None
    type: str = Field(..., pattern="^(income|expense)$")
    category_id: int

class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    description: str | None = None
    type: str
    category_id: int

    class Config:
        from_attributes = True