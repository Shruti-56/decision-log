from pydantic import BaseModel
from datetime import datetime

class DecisionCreate(BaseModel):
    title: str
    context: str
    options: str
    final_decision: str
    reason: str

class DecisionResponse(DecisionCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
