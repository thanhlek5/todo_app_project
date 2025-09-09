from sqlmodel import Session
from models.model import User
def get_user_by_username(db_session:Session,username: str) -> bool:
    """
    hàm để kiểm tra là username đã tồn tại chưa.
    trả về true nếu usename đó chưa đc dùng và có thể sử dụng.
    trả về false nếu username đã tồn tại.
    """
    exit_user  = db_session.query(User).filter(User.username == username).first()
    return exit_user is None