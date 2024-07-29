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
    expense = create_expense(db=db, expense_in=expense_in, user_id=expense_in.created_by)
    return expense

@router.get("/user/{user_id}", response_model=list[Expense])
def read_user_expenses(user_id: str, db: Session = Depends(get_db)):
    expenses = get_user_expenses(db=db, user_id=user_id)
    if not expenses:
        raise HTTPException(status_code=404, detail="Expenses not found")
    return expenses

@router.get("/", response_model=list[Expense])
def read_all_expenses(db: Session = Depends(get_db)):
    expenses = get_all_expenses(db=db)
    return expenses

@router.get("/balance-sheet")
def download_balance_sheet(db: Session = Depends(get_db)):
    balance_sheet_csv = generate_balance_sheet(db)
    response = StreamingResponse(
        io.StringIO(balance_sheet_csv),
        media_type="text/csv"
    )
    response.headers["Content-Disposition"] = "attachment; filename=balance_sheet.csv"
    return response