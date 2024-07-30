from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid

class SplitType(str):
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

class Expense(Base):
    """
    Model representing an expense.
    
    Attributes:
        id (str): Unique identifier for the expense.
        description (str): Description of the expense.
        amount (float): Total amount of the expense.
        split_type (str): Method of splitting the expense (equal, exact, percentage).
        created_by (str): User ID of the creator of the expense.
        created_at (str): Timestamp of when the expense was created.
        
    Relationships:
        participants (relationship): Relationship to the ExpenseParticipant model.
    """
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    split_type = Column(String, nullable=False)
    created_by = Column(String, ForeignKey('user.id'), nullable=False)
    created_at = Column(String, nullable=False)

    # Relationships
    participants = relationship("ExpenseParticipant", back_populates="expense")

class ExpenseParticipant(Base):
    """
    Model representing a participant in an expense.
    
    Attributes:
        id (str): Unique identifier for the expense participant.
        user_id (str): User ID of the participant.
        expense_id (str): Expense ID associated with the participant.
        amount (float, optional): Exact amount the participant owes (for exact and percentage splits).
        percentage (float, optional): Percentage of the total amount the participant owes (for percentage splits).
        
    Relationships:
        expense (relationship): Relationship to the Expense model.
        user (relationship): Relationship to the User model.
    """
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey('user.id'), nullable=False)
    expense_id = Column(String, ForeignKey('expense.id'), nullable=False)
    amount = Column(Float, nullable=True)
    percentage = Column(Float, nullable=True)

    # Relationships
    expense = relationship("Expense", back_populates="participants")
    user = relationship("User")
