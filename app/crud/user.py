from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
import uuid

def get_user_by_email(db: Session, email: str):
    """
    Retrieve a user by their email address.

    Args:
        db (Session): The database session.
        email (str): The email address of the user.

    Returns:
        User: The user details if found, else None.
    """
    return db.query(User).filter(User.email == email).first()

def get_user(db: Session, user_id: str):
    """
    Retrieve a user by their ID.

    Args:
        db (Session): The database session.
        user_id (str): The ID of the user.

    Returns:
        User: The user details if found, else None.
    """
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user_in: UserCreate):
    """
    Create a new user with validated email and mobile number.

    Args:
        db (Session): The database session.
        user_in (UserCreate): The user information.

    Returns:
        User: The created user.
    
    Raises:
        ValueError: If the email or mobile number is invalid.
    """
    # Validate email and mobile number using Pydantic schema
    user_in = UserCreate(**user_in.dict())

    db_user = User(
        id=str(uuid.uuid4()),
        email=user_in.email,
        name=user_in.name,
        mobile_number=user_in.mobile_number,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user