
from datetime import datetime

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_root_endpoint_returns_welcome_message():
    response = client.get("/")
    data = response.json()

    assert data["message"] == "Welcome to ManufactureFlow AI"
    assert data["project"] == "ManufactureFlow AI"


def test_root_endpoint_status_is_running():
    response = client.get("/")
    assert response.json()["status"] == "running"


def test_health_endpoint_returns_200():
    response = client.get("/health")
    assert response.status_code == 200


def test_health_endpoint_status_is_healthy():
    response = client.get("/health")
    assert response.json()["status"] == "healthy"


def test_health_endpoint_application_name():
    response = client.get("/health")
    assert response.json()["application"] == "ManufactureFlow AI"


def test_health_endpoint_has_valid_timestamp():
    response = client.get("/health")
    timestamp = response.json()["timestamp"]

    # This raises ValueError if the timestamp is invalid.
    parsed_timestamp = datetime.fromisoformat(timestamp)

    assert parsed_timestamp is not None


def test_api_documentation_is_available():
    response = client.get("/docs")
    assert response.status_code == 200

