from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
import uuid

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user_in: UserCreate):
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
