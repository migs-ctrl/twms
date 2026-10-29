from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Client(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    dob = Column(String,nullable=False)
    address = Column(String,nullable=True)
    phone = Column(String,nullable=True)
    email = Column(String,nullable=True)
    def __repr__(self):
        return 'ClientModel(first_name=%s, last_name=%s,dob=%s,phone=%s,email=%s, address=%s)' % (self.first_name, self.last_name, self.dob, self.phone, self.email, self.address)

class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String,nullable=False)

    def __repr__(self):
        return 'ClientModel(employee_name=%s)' % ( self.employee_name)