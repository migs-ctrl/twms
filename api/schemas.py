from pydantic import BaseModel
from typing import Optional
name: Optional[str] = None

class ClientBase(BaseModel):
    client_id: Optional[int] = None
    first_name: str
    last_name: str
    address: Optional[str] = None
    dob: str
    phone: str
    email: Optional[str] = None


class ClientCreate(ClientBase):
    pass

class GetClient(ClientBase):
    pass

class Client(ClientBase):
    client_id: Optional[int] = None
    first_name: str
    last_name: str
    dob: str
    address: Optional[str] = None
    phone: str
    email: Optional[str] = None

    class Config:
        orm_mode = True


class EmployeeBase(BaseModel):
    employee_id: Optional[int] = None
    employee_name: str


class GetEmployee(EmployeeBase):
    pass


class Employee(EmployeeBase):
    employee_id: Optional[int] = None
    employee_name: str

    class Config:
        orm_mode = True