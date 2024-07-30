from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from app.crud.expense import create_expense, get_user_expenses, get_all_expenses, generate_balance_sheet
from app.schemas.expense import Expense, ExpenseCreate
from app.db.session import get_db
import io

router = APIRouter()

@router.post("/", response_model=Expense)
def create_expense_endpoint(
    expense_in: ExpenseCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new expense.

    Args:
        expense_in (ExpenseCreate): The expense information.
        db (Session): The database session.

    Returns:
        Expense: The created expense.
    """
    expense = create_expense(db=db, expense_in=expense_in, user_id=expense_in.created_by)
    return expense

@router.get("/user/{user_id}", response_model=list[Expense])
def read_user_expenses(user_id: str, db: Session = Depends(get_db)):
    """
    Retrieve expenses for a specific user by user ID.

    Args:
        user_id (str): The user ID.
        db (Session): The database session.

    Returns:
        list[Expense]: A list of expenses for the user.
    
    Raises:
        HTTPException: If no expenses are found for the user.
    """
    expenses = get_user_expenses(db=db, user_id=user_id)
    if not expenses:
        raise HTTPException(status_code=404, detail="Expenses not found")
    return expenses

@router.get("/", response_model=list[Expense])
def read_all_expenses(db: Session = Depends(get_db)):
    """
    Retrieve all expenses.

    Args:
        db (Session): The database session.

    Returns:
        list[Expense]: A list of all expenses.
    """
    expenses = get_all_expenses(db=db)
    return expenses

@router.get("/balance-sheet")
def download_balance_sheet(db: Session = Depends(get_db)):
    """
    Download the balance sheet as a CSV file.

    Args:
        db (Session): The database session.

    Returns:
        StreamingResponse: The CSV file containing the balance sheet.
    """
    balance_sheet_csv = generate_balance_sheet(db)
    response = StreamingResponse(
        io.StringIO(balance_sheet_csv),
        media_type="text/csv"
    )
    response.headers["Content-Disposition"] = "attachment; filename=balance_sheet.csv"
    return response