from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel
from datetime import datetime, date
class LoginRequest(BaseModel):
    username: str
    password: str 

class CreateUser(BaseModel):
    username: str 
    password: str
    email: EmailStr

class User(BaseModel):
    id: int
    username: str
    hash_pass: str
    email: EmailStr

class Task(BaseModel):
    id: int 
    user_id : int
    color_id : int
    priority_id : int
    project_id : int
    name : str
    description : str
    status : str 
    create_at : datetime
    update_at: datetime
    complete_at : datetime
    start_date: date
    due_date: date

class Create_Task(SQLModel):
    name :str
    description :str
class Read_Task(SQLModel):
    id : int
    user_id: int
    name : str 
    description: str
    status : str
    priority_id :int
class Subtask(BaseModel):
    id : int 
    name :str
    decription : str
    status : str 
    task_id :int
    color_id :int
    priority_id :int