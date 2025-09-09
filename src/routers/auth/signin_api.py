from services.signin_service import signin
from schema import LoginRequest
from fastapi import Depends, HTTPException,APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_session

router = APIRouter()

@router.post('/login')
def login_endpoint(request: LoginRequest):
    
    is_successful = signin(
            db_session= Session,
            username= request.username, 
            password= request.password
            )
    if not is_successful:
        raise HTTPException(status_code=401, detail= 'Thông tin đăng nhập không chính xác.')
    return {"message": "Đăng nhập thành công"}



