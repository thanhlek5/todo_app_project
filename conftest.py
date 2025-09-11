# d:
# \todo_app\conftest.py

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine

# --- ADD THIS LINE ---
# This ensures that Python and SQLModel are aware of your models.
# Make sure the import path is correct.
from src.models import model 

from src.main import app
from src.database import get_session # Or get_session, depending on your setup

# (The rest of your file remains the same)
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

def override_get_db(): # Or override_get_session
    with Session(engine) as session:
        yield session

app.dependency_overrides[get_session] = override_get_db # Or get_session

@pytest.fixture(scope="function")
def client():
    SQLModel.metadata.create_all(engine)
    with TestClient(app) as c:
        yield c
    SQLModel.metadata.drop_all(engine)