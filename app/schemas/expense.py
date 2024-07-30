from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class SplitType(str, Enum):
    """
    Enumeration for different types of expense splits.

    Attributes:
        EQUAL (str): Equal split among participants.
        EXACT (str): Exact amount specified for each participant.
        PERCENTAGE (str): Percentage specified for each participant.
    """
    EQUAL = "equal"
    EXACT = "exact"
    PERCENTAGE = "percentage"

class ExpenseParticipantBase(BaseModel):
    """
    Base model for expense participant.

    Attributes:
        user_id (str): ID of the user.
        amount (Optional[float]): Exact amount owed by the participant. Optional.
        percentage (Optional[float]): Percentage of the total amount owed by the participant. Optional.
    """
    user_id: str
    amount: Optional[float] = None
    percentage: Optional[float] = None

class ExpenseParticipantCreate(ExpenseParticipantBase):
    """
    Schema for creating a new expense participant.
    Inherits all attributes from ExpenseParticipantBase.
    """
    pass

class ExpenseParticipant(ExpenseParticipantBase):
    """
    Model for expense participant.

    Attributes:
        id (str): Unique identifier for the expense participant.
    """
    id: str

    class Config:
        orm_mode = True

class ExpenseBase(BaseModel):
    """
    Base model for expense.

    Attributes:
        description (str): Description of the expense.
        amount (float): Total amount of the expense.
        split_type (SplitType): Method of splitting the expense (equal, exact, percentage).
    """
    description: str
    amount: float
    split_type: SplitType

class ExpenseCreate(ExpenseBase):
    """
    Schema for creating a new expense.

    Attributes:
        participants (List[ExpenseParticipantCreate]): List of participants in the expense.
        created_by (str): ID of the user who created the expense.
    """
    participants: List[ExpenseParticipantCreate]
    created_by: str

class Expense(ExpenseBase):
    """
    Model for expense.

    Attributes:
        id (str): Unique identifier for the expense.
        created_by (str): ID of the user who created the expense.
        participants (List[ExpenseParticipant]): List of participants in the expense.
    """
    id: str
    created_by: str
    participants: List[ExpenseParticipant]

    class Config:
        orm_mode = True
