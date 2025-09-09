from sqlmodel import Session
from models.model import User
from utils.validation import get_user_by_username
from werkzeug.security import generate_password_hash 


def add_new_user(db_session: Session, username: str, password: str, email: str) -> User:
    """
    Thêm một người dùng vào cơ sở dữ liệu.
    Nhận vào 1 sesion đang hoạt động.
    """
    
    exit_user = get_user_by_username(db_session,username)
    if not exit_user:
        raise ValueError(f'Username {username} đã được sử đụng.')
    
    hash_pass = generate_password_hash(password=password)
    
    print(f'Adding user {username} to the database')
    new_user =User(username=username, hash_pass= hash_pass,email=email)
    
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    
    return new_user