from src.services.signup_service import add_new_user
from src.schema import CreateUser
from fastapi import APIRouter, HTTPException, Depends 
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from src.database import get_session
router = APIRouter()

@router.post('/signup')
def new_user_endpoint(request : CreateUser, db : Session = Depends(get_session)):
    is_successful = add_new_user(       # -> bool
        db_session= db,
        username= request.username,
        password= request.password,
        email= request.email
    )

    if not is_successful: 
        raise HTTPException(
            status_code=401,
            detail='Tài khoản đã tồn tại!'
        )
    return JSONResponse(
        status_code=200,
        content=({'message':'Đăng ký thành công.'})
    )
