from typing import List
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas.contacts import ContactModel, ContactUpdate, ContactEmailUpdate


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()



async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def get_contact_by_fields(first_name: str,
                               last_name: str,
                               phone: str,
                               email: str,
                               days_before_birth: int,
                               db: Session) -> List[Contact]:
    
    contact = db.query(Contact)
    
    if first_name:
        contact = contact.filter(Contact.first_name == first_name)
        
    if last_name:
        contact = contact.filter(Contact.last_name == last_name)
    
    if phone:
        contact = contact.filter(Contact.phone == phone)
        
    if email:
        contact = contact.filter(Contact.email == email)        
    
    start_date = datetime.now()
    end_date = start_date + timedelta(days=days_before_birth)     
    contact = contact.filter(Contact.birthday.between(start_date, end_date))
    
    return contact.all()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(**vars(body))
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, db: Session):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    
    if contact:        
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.phone = body.phone
        contact.email = body.email
        contact.birthday = body.birthday
        db.commit()
        
    return contact


async def update_email_contact(contact_id: int, body: ContactEmailUpdate, db: Session):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    
    if contact:
        contact.email = body.email
        db.commit()
        
    return contact


async def remove_contact(contact_id: int, db: Session):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    
    if contact:
        db.delete(contact)
        db.commit()
        
    return contact