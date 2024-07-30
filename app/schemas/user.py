from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """
    Base model for user.

    Attributes:
        email (EmailStr): Email address of the user.
        name (str): Name of the user.
        mobile_number (str): Mobile number of the user.
    """
    email: EmailStr
    name: str
    mobile_number: str

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
