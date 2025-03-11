from fastapi.testclient import TestClient
from app.main import app
from db.session import get_db, SessionLocal

client = TestClient(app)

def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Test Description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task():
    response = client.put("/tasks/1", json={"title": "Updated Task", "description": "Updated Desc"})
    assert response.status_code in [200, 404]  # Ensure it either updates or shows not found

def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code in [200, 404]
