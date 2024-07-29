from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class SplitType(str, Enum):
    EQUAL = "equal"
    EXACT = "exact"
    PERCENTAGE = "percentage"

class ExpenseParticipantBase(BaseModel):
    user_id: str
    amount: Optional[float] = None
    percentage: Optional[float] = None

class ExpenseParticipantCreate(ExpenseParticipantBase):
    pass

class ExpenseParticipant(ExpenseParticipantBase):
    id: str

    class Config:
        orm_mode = True

class ExpenseBase(BaseModel):
    description: str
    amount: float
    split_type: SplitType

class ExpenseCreate(ExpenseBase):
    participants: List[ExpenseParticipantCreate]
    created_by: str

class Expense(ExpenseBase):
    id: str
    created_by: str
    participants: List[ExpenseParticipant]

    class Config:
        orm_mode = True
