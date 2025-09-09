from sqlmodel import SQLModel, create_engine, Session

# đường dẫn đến file lưu trữ database 
sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///D:/todo_app/Instance/{sqlite_file_name}'

engine = create_engine(sqlite_url, echo =True)


def create_db_and_tables():
    """Hàm này dùng để tạo bảng và db"""
    from models import model 
    
    print('Đang khởi tạo database và các bảng...')
    SQLModel.metadata.create_all(engine)
    print('Database và bảng đã được khởi tạo thành công.')

def get_session():
    """
    Hàm tạo ra một phiên làm việc (session) để tương tác với CSDL.
    """
    with Session(engine) as session:
        yield session