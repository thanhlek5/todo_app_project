from sqlmodel import Session
from src.models.model import User
from werkzeug.security import check_password_hash


def signin(db_session : Session, username: str, password: str)-> bool:
    """
    hàm dùng để đăng nhập tài khoản.
    trả về true nếu tên tài khoản và mật khẩu trùng khớp.
    trả về false nếu không có tài khoản nào có trùng thông tin với thông tin đăng nhập (tài khoản không tồn tại.)
    """
    user = db_session.query(User).filter(User.username == username).first()   # -> User
    if not user or not check_password_hash(password= password, pwhash= user.hash_pass) : 
        return False 
    
    return True
    
    
    