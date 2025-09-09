# test_auth.py
import pytest
from fastapi.testclient import TestClient
from src.main import app # Import đối tượng app chính

# --- Fixtures: Công cụ chuẩn bị cho các bài test ---

@pytest.fixture(scope="module")
def client():
    """
    Tạo một TestClient cho toàn bộ module test này.
    Điều này giúp sử dụng lại client thay vì tạo mới cho mỗi test.
    """
    with TestClient(app) as c:
        yield c

@pytest.fixture
def setup_test_user(client: TestClient):
    """
    Một fixture để đăng ký một người dùng mới trước khi test đăng nhập.
    Nó sẽ tự động chạy trước mỗi test cần nó.
    """
    user_data = {
        "username": "testuser_signin",
        "email": "testsignin@example.com",
        "password": "correct_password"
    }
    # Đăng ký người dùng này để chuẩn bị cho các test đăng nhập
    client.post("/auth/signup", json=user_data)
    return user_data # Trả về dữ liệu để các test khác có thể dùng

# --- Các bài test ---

def test_signup_successfully(client: TestClient):
    """
    Kiểm tra trường hợp đăng ký người dùng mới thành công.
    """
    new_user_data = {
        "username": "new_user",
        "email": "new_user@example.com",
        "password": "a_valid_password"
    }
    response = client.post("/auth/signup", json=new_user_data)
    
    # Khi tạo mới thành công, status code phải là 201 Created
    assert response.status_code == 201
    assert response.json()["message"] == "Đăng ký thành công."

def test_signup_existing_user(client: TestClient):
    """
    Kiểm tra trường hợp đăng ký một người dùng đã tồn tại.
    """
    existing_user_data = {
        "username": "existing_user",
        "email": "existing@example.com",
        "password": "password123"
    }
    # Gọi lần 1 để tạo user
    client.post("/auth/signup", json=existing_user_data)
    # Gọi lần 2 với cùng dữ liệu để gây ra lỗi
    response = client.post("/auth/signup", json=existing_user_data)

    # Khi bị trùng lặp, status code phải là 409 Conflict
    assert response.status_code == 409
    assert "Tài khoản hoặc email đã tồn tại!" in response.json()["detail"]

def test_signin_successful(client: TestClient, setup_test_user):
    """
    Kiểm tra trường hợp đăng nhập thành công.
    Fixture 'setup_test_user' sẽ chạy trước, đảm bảo user đã tồn tại.
    """
    login_data = {
        "username": setup_test_user["username"],
        "password": setup_test_user["password"]
    }
    response = client.post('/auth/signin', json=login_data)
    
    # Khi đăng nhập thành công, status code phải là 200 OK
    assert response.status_code == 200
    assert response.json()["message"] == 'Đăng nhập thành công.'

def test_signin_unsuccessful_wrong_password(client: TestClient, setup_test_user):
    """
    Kiểm tra trường hợp đăng nhập thất bại do sai mật khẩu.
    """
    login_data = {
        "username": setup_test_user["username"],
        "password": "wrong_password" # Mật khẩu sai
    }
    response = client.post('/auth/signin', json=login_data)
    
    # Khi xác thực thất bại, status code phải là 401 Unauthorized
    assert response.status_code == 401
    assert "Tên đăng nhập hoặc mật khẩu không chính xác" in response.json()["detail"]