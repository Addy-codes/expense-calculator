from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid

class User(Base):
    """
    Model representing a user.
    
    Attributes:
        id (str): Unique identifier for the user.
        email (str): Email address of the user.
        name (str): Name of the user.
        mobile_number (str): Mobile number of the user.
    """
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    mobile_number = Column(String, index=True, nullable=False)