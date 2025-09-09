# from sqlmodel import SQLModel, Session,select
# from models.model import User
# from services import signup_service
# from database import engine, create_db_and_tables

# def run_app():
#     """
#     Hàm chính dùng để điều phối app
#     """
#     #  tạo session duy nhất để truyền vào hàm service
#     with Session(engine) as session:
        
#         print("\n--- Thử thêm người dùng mới ---")
#         signup_service.add_new_user(
#             db_session=session, 
#             username="test01", 
#             email="test01@example.com", 
#             password="1234"
#         )
    
# if __name__ == '__main__':
#     #   khởi tạo csdl 
#     create_db_and_tables()
#     run_app()

# main.py

from fastapi import FastAPI
from src.routers.auth import signin_api, signup_api
# Bạn có thể import thêm các thành phần khác nếu cần, ví dụ như database
# from database import engine, Base

# Khởi tạo ứng dụng FastAPI
# Bạn có thể thêm các thông tin mô tả cho API của mình
app = FastAPI(
    title="Todo App API",
    description="API để quản lý ứng dụng công việc cá nhân.",
    version="1.0.0",
)

# --- LẮP RÁP CÁC ROUTER ---
# Đây là bước quan trọng nhất trong file main.py
# Nó "gắn" tất cả các endpoint bạn đã định nghĩa trong các file API
# vào ứng dụng chính để chúng có thể được truy cập.

# Gắn các API liên quan đến đăng ký (signup)
app.include_router(
    signup_api.router,
    prefix="/auth", # Tiền tố chung cho nhóm API này
    tags=["Authentication"] # Gom nhóm API trong trang tài liệu docs
)

# Gắn các API liên quan đến đăng nhập (signin)
app.include_router(
    signin_api.router,
    prefix="/auth", # Dùng chung tiền tố để các API xác thực có chung đường dẫn gốc
    tags=["Authentication"] # Dùng chung tag để gom nhóm
)


# --- ENDPOINT GỐC (TÙY CHỌN) ---
# Một endpoint đơn giản để kiểm tra xem server có đang hoạt động không.
# Bạn có thể truy cập vào địa chỉ http://127.0.0.1:8000 để xem kết quả.
@app.get("/")
def read_root():
    """
    Endpoint chào mừng của ứng dụng.
    """
    return {"message": "Welcome to the Todo App API!"}


# --- CÁC THIẾT LẬP KHÁC (VÍ DỤ) ---
# Nếu bạn dùng SQLAlchemy, bạn có thể thêm lệnh tạo bảng ở đây
# để đảm bảo các bảng trong CSDL được tạo ra khi ứng dụng khởi động.
#
# @app.on_event("startup")
# def on_startup():
#     Base.metadata.create_all(bind=engine)