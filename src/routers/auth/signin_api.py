from src.services.signin_service import signin
from src.schema import LoginRequest
from fastapi import  HTTPException,APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.database import get_session

router = APIRouter()

@router.post('/login')
def login_endpoint(request: LoginRequest, db: Session = Depends(get_session) ):
    
    is_successful = signin(
            db_session= db,
            username= request.username, 
            password= request.password
            )
    if not is_successful:
        raise HTTPException(
            status_code=404, 
            detail= 'Thông tin đăng nhập không chính xác.')
    return JSONResponse(
        status_code=200,
        content= {"message": "Đăng nhập thành công"})



