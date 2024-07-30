from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.user import(
    get_user,
    get_user_by_email,
    create_user
)
from app.schemas.user import(
    User,
    UserCreate
)
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=User)
def write_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.

    Args:
        user_in (UserCreate): The user information.
        db (Session): The database session.

    Returns:
        User: The created user.
    
    Raises:
        HTTPException: If the email is already registered.
    """
    db_user = get_user_by_email(db, email=user_in.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = create_user(db=db, user_in=user_in)
    return user

@router.get("/{user_id}", response_model=User)
def read_user(user_id: str, db: Session = Depends(get_db)):
    """
    Retrieve user details by user ID.

    Args:
        user_id (str): The user ID.
        db (Session): The database session.

    Returns:
        User: The user details.
    
    Raises:
        HTTPException: If the user is not found.
    """
    user = get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
