from sqlmodel import SQLModel, Session,select
from models.model import User
from services import signup_service
from database import engine, create_db_and_tables

def run_app():
    """
    Hàm chính dùng để điều phối app
    """
    #  tạo session duy nhất để truyền vào hàm service
    with Session(engine) as session:
        
        print("\n--- Thử thêm người dùng mới ---")
        signup_service.add_new_user(
            db_session=session, 
            username="test01", 
            email="test01@example.com", 
            password="1234"
        )
    
if __name__ == '__main__':
    #   khởi tạo csdl 
    create_db_and_tables()
    run_app()