from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field, EmailStr, constr


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    password: str = Field(min_length=6, max_length=10)
    email: Optional[EmailStr]
    phone: Optional[
        constr(
            strip_whitespace=True,
            regex=r"^(\+)[1-9][0-9\-\(\)]{9,18}$",
        )
    ]
    
    
class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    username: str = Field(min_length=5, max_length=16)
    birthday: Optional[date]
    job: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[
        constr(
            strip_whitespace=True,
            regex=r"^(\+)[1-9][0-9\-\(\)]{9,18}$",
        )
    ]    
    

class UserDB(UserUpdate):
    id: int
    created_at: datetime
    avatar: str
    
    class Config:
        orm_mode = True
        
        
class UserResponse(BaseModel):
    user: UserDB
    detail: str = "User seccessfully created"
    

class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    