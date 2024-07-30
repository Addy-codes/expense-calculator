from pydantic import BaseModel, EmailStr, validator
from typing import Optional
import re

class UserBase(BaseModel):
    """
    Base model for user with validation for email and mobile number.

    Attributes:
        email (EmailStr): Email address of the user.
        name (str): Name of the user.
        mobile_number (str): Mobile number of the user.
    """
    email: EmailStr
    name: str
    mobile_number: str

    @validator('mobile_number')
    def validate_mobile_number(cls, v):
        """
        Validate that the mobile number is between 10 to 15 digits and can include an optional + prefix.

        Args:
            v (str): The mobile number.

        Returns:
            str: The validated mobile number.

        Raises:
            ValueError: If the mobile number is invalid.
        """
        if not re.match(r'^\+?\d{10,15}$', v):
            raise ValueError('Mobile number must be between 10 to 15 digits and can include an optional + prefix')
        return v
class UserCreate(UserBase):
    """
    Schema for creating a new user.
    Inherits all attributes from UserBase.
    """
    pass

class UserInDBBase(UserBase):
    """
    Base model for user in database.

    Attributes:
        id (str): Unique identifier for the user.
    """
    id: str

    class Config:
        orm_mode = True

class User(UserInDBBase):
    """
    Model for user.
    Inherits all attributes from UserInDBBase.
    """
    pass

class UserInDB(UserInDBBase):
    """
    Model for user in database.
    Inherits all attributes from UserInDBBase.
    """
    pass
