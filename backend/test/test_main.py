import pytest
from fastapi.testclient import TestClient
from ..main import app, items, Item  # 相対インポートを使用


@pytest.fixture(scope="module")
def client():
    return TestClient(app)

def test_create_item(client):
    response = client.post("/items/", json={"id": 4, "name": "Item 4", "description": "Description for Item 4", "price": 40.0, "tax": 4.0})
    assert response.status_code == 200
    assert response.json() == {"id": 4, "name": "Item 4", "description": "Description for Item 4", "price": 40.0, "tax": 4.0}

def test_read_items(client):
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) == len(items)

def test_read_item(client):
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Item 1", "description": "Description for Item 1", "price": 10.0, "tax": 1.0}

def test_read_nonexistent_item(client):
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_update_item(client):
    response = client.put("/items/1", json={"id": 1, "name": "Updated Item 1", "description": "Updated Description for Item 1", "price": 100.0, "tax": 10.0})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Updated Item 1", "description": "Updated Description for Item 1", "price": 100.0, "tax": 10.0}

def test_delete_item(client):
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Item deleted"}
    response = client.get("/items/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}