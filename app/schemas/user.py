from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    name: str
    mobile_number: str

class UserCreate(UserBase):
    pass

class UserInDBBase(UserBase):
    id: str

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    pass
