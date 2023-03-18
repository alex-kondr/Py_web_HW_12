from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel, Field, EmailStr, constr


class ContactBase(BaseModel):
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    email: Optional[EmailStr]    
    phone: Optional[
        constr(
            strip_whitespace=True,
            regex=r"^(\+)[1-9][0-9\-\(\)]{9,16}$",
        )
    ]
      
        
class ContactModel(ContactBase):
    birthday: Optional[date]
    
    
class ContactUpdate(ContactModel):
    pass


class ContactEmailUpdate(BaseModel):
    email: Optional[EmailStr]
    

class ContactResponse(ContactModel):
    id: int
    create_at: datetime
    
    class Config:
        orm_mode = True