from sqlalchemy.orm import Session
from app.models.expense import Expense, ExpenseParticipant, SplitType
from app.models.user import User
from app.schemas.expense import ExpenseCreate
from app.schemas.expense import ExpenseParticipant as ExpenseParticipantSchema
import uuid
import csv
from io import StringIO
from datetime import datetime

def create_expense(db: Session, expense_in: ExpenseCreate, user_id: str):
    """
    Create a new expense and distribute the amount among participants based on the split type.

    Args:
        db (Session): The database session.
        expense_in (ExpenseCreate): The expense information.
        user_id (str): The ID of the user who created the expense.

    Returns:
        Expense: The created expense.
    """
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
    """
    Retrieve an expense by its ID.

    Args:
        db (Session): The database session.
        expense_id (str): The ID of the expense.

    Returns:
        Expense: The expense details.
    """
    return db.query(Expense).filter(Expense.id == expense_id).first()

def get_user_expenses(db: Session, user_id: str):
    """
    Retrieve all expenses for a specific user.

    Args:
        db (Session): The database session.
        user_id (str): The ID of the user.

    Returns:
        list[Expense]: A list of expenses for the user.
    """
    return db.query(Expense).join(ExpenseParticipant).filter(ExpenseParticipant.user_id == user_id).all()

def get_all_expenses(db: Session):
    """
    Retrieve all expenses.

    Args:
        db (Session): The database session.

    Returns:
        list[Expense]: A list of all expenses.
    """
    return db.query(Expense).all()

def generate_balance_sheet(db: Session):
    """
    Generate a balance sheet CSV file containing all expenses and participants' details.

    Args:
        db (Session): The database session.

    Returns:
        str: The CSV content as a string.
    """
    output = StringIO()
    writer = csv.writer(output)

    # Write header
    writer.writerow(['Expense ID', 'Description', 'Amount', 'Split Type', 'Created By', 'Created At'])

    # Fetch all expenses
    expenses = db.query(Expense).all()
    for expense in expenses:
        writer.writerow([
            expense.id,
            expense.description,
            expense.amount,
            expense.split_type,
            expense.created_by,
            expense.created_at
        ])

    # Fetch individual expenses
    writer.writerow([])
    # Write header
    writer.writerow(['User ID', 'Name', 'Expense ID', 'Amount', 'Percentage'])

    # Fetch all expenses and participants, including user names
    results = db.query(
        ExpenseParticipant.user_id,
        User.name,
        ExpenseParticipant.expense_id,
        ExpenseParticipant.amount,
        ExpenseParticipant.percentage
    ).join(User, User.id == ExpenseParticipant.user_id).all()

    for result in results:
        writer.writerow([
            result.user_id,
            result.name,
            result.expense_id,
            result.amount,
            result.percentage
        ])

    output.seek(0)
    return output.getvalue()