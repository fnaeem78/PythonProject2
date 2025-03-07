import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is in a file named main.py

client = TestClient(app)

def test_read_root_default():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, World!"
    assert "decorated" not in data  # Ensure the decorator applied the field

def test_read_root_with_decorate_false():
    # read eval plan, qa eval plan and data set
    # read data set
    # read query per test or all in a data set
    # now build state and call pgsql retriever step
    # the decorator should run and put things in the database.
    # optionally verify that what was put in the database is within limits of tolerance
    response = client.get("/?decorate=false")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, World!"
    assert "decorated_condition" in data
    assert data["decorated_condition"] is False

def test_read_root_with_decorate_true():
    response = client.get("/?decorate=true")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, World!"
    assert "decorated_condition" in data
    assert data["decorated_condition"] is True