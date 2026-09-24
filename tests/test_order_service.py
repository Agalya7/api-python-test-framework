import pytest

from api.api_client import APIClient


BASE_URL = "http://127.0.0.1:8001"


@pytest.fixture
def order_api_client():
    return APIClient(BASE_URL)


def test_create_order(order_api_client):
    payload = {
        "product_id": 101,
        "quantity": 2,
        "amount": 49.99
    }

    response = order_api_client.post("/orders", payload)

    assert response.status_code == 200

    order = response.json()

    assert order["order_id"] == 1
    assert order["product_id"] == payload["product_id"]
    assert order["quantity"] == payload["quantity"]
    assert order["status"] == "created"
    assert order["payment_status"] == "approved"
