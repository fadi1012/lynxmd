import os

import pytest
from fastapi.testclient import TestClient
from app.event_routes import app

client = TestClient(app)

# Assuming this file is in the 'tests' directory
test_dir = os.path.dirname(os.path.abspath(__file__))
static_dir_path = os.path.join(test_dir, "../static")

# Define test cases with parameters for response and description
test_cases = [
    ("/events/countByEventType", 200, {"foo": 3, "bar": 1}, "Count of events by event type (countByEventType)"),
    ("/events/CountWords", 200, {"lorem": 2, "ipsum": 1}, "Count of events by event type (countWords)"),
]


@pytest.fixture
def client_with_static_path(monkeypatch):
    # Monkeypatch the app's static directory path to include your 'static' directory
    monkeypatch.setattr(app, "static_dir", static_dir_path)
    client = TestClient(app)
    return client


@pytest.mark.parametrize("endpoint, status_code, expected_response, expected_description", test_cases)
def test_endpoint(endpoint, status_code, expected_response, expected_description):
    response = client.get(endpoint)
    assert response.status_code == status_code
    data = response.json()
    assert data == expected_response
    assert app.routes[0].path == endpoint  # Verify that the correct route is associated with the endpoint
    assert app.routes[0].endpoint.__doc__ == expected_description  # Verify the endpoint's description
