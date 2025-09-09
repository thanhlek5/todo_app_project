from pydantic import BaseModel, EmailStr

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


