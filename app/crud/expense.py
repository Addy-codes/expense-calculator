from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.expense import Expense, ExpenseParticipant, SplitType
from app.schemas.expense import ExpenseCreate
from app.schemas.expense import ExpenseParticipant as ExpenseParticipantSchema
import uuid
from datetime import datetime

def create_expense(db: Session, expense_in: ExpenseCreate, user_id: str):
    print(f"Creating expense with description: {expense_in.description}, amount: {expense_in.amount}, split_type: {expense_in.split_type}")
    print(SplitType.EQUAL)
    expense_id = str(uuid.uuid4())
    expense = Expense(
        id=expense_id,
        description=expense_in.description,
        amount=expense_in.amount,
        split_type=expense_in.split_type,
        created_by=user_id,
        created_at=str(datetime.utcnow())
    )
    db.add(expense)
    
    total_amount = expense_in.amount
    if expense_in.split_type == SplitType.EQUAL:
        per_person_amount = total_amount / len(expense_in.participants)
        for participant in expense_in.participants:
            expense_participant = ExpenseParticipant(
                id=str(uuid.uuid4()),
                user_id=participant.user_id,
                expense_id=expense_id,
                amount=per_person_amount
            )
            db.add(expense_participant)
    elif expense_in.split_type == SplitType.EXACT:
        for participant in expense_in.participants:
            expense_participant = ExpenseParticipant(
                id=str(uuid.uuid4()),
                user_id=participant.user_id,
                expense_id=expense_id,
                amount=participant.amount
            )
            db.add(expense_participant)
    elif expense_in.split_type == SplitType.PERCENTAGE:
        for participant in expense_in.participants:
            expense_participant = ExpenseParticipant(
                id=str(uuid.uuid4()),
                user_id=participant.user_id,
                expense_id=expense_id,
                percentage=participant.percentage,
                amount=(participant.percentage / 100) * total_amount
            )
            db.add(expense_participant)

    db.commit()
    db.refresh(expense)
    return expense


def get_expense(db: Session, expense_id: str):
    return db.query(Expense).filter(Expense.id == expense_id).first()

def get_user_expenses(db: Session, user_id: str):
    return db.query(Expense).join(ExpenseParticipant).filter(ExpenseParticipant.user_id == user_id).all()

def get_all_expenses(db: Session):
    return db.query(Expense).all()
