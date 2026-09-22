import pytest

from api.api_client import APIClient


BASE_URL = "http://127.0.0.1:8002"


@pytest.fixture
def payment_api_client():
    return APIClient(BASE_URL)


def test_create_payment(payment_api_client):
    payload = {
        "order_id": 1,
        "amount": 49.99
    }

    response = payment_api_client.post("/payments", payload)

    assert response.status_code == 200

    payment = response.json()

    assert payment["payment_id"] == 1
    assert payment["order_id"] == payload["order_id"]
    assert payment["amount"] == payload["amount"]
    assert payment["status"] == "approved"
