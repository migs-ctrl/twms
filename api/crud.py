from sqlalchemy.orm import Session

import models, schemas

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).all()

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(first_name=client.first_name, last_name=client.last_name, dob= client.dob, email=client.email, address=client.address, phone=client.phone)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()