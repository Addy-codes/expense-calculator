from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid

class SplitType(str):
    EQUAL = "equal"
    EXACT = "exact"
    PERCENTAGE = "percentage"

class Expense(Base):
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    split_type = Column(String, nullable=False)
    created_by = Column(String, ForeignKey('user.id'), nullable=False)
    created_at = Column(String, nullable=False)

    # Relationships
    participants = relationship("ExpenseParticipant", back_populates="expense")

class ExpenseParticipant(Base):
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey('user.id'), nullable=False)
    expense_id = Column(String, ForeignKey('expense.id'), nullable=False)
    amount = Column(Float, nullable=True)
    percentage = Column(Float, nullable=True)

    # Relationships
    expense = relationship("Expense", back_populates="participants")
    user = relationship("User")
