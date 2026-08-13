from calculator import divide
from server import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_divide():
    client = app.test_client()
    response = client.post("/divide", json={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.get_json() == {"result": 5.0}

def test_divide_by_zero():
    client = app.test_client()
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Cannot divide by zero"}