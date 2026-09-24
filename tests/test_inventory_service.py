import pytest

from api.api_client import APIClient


BASE_URL = "http://127.0.0.1:8003"


@pytest.fixture
def inventory_api_client():
    return APIClient(BASE_URL)


def test_check_inventory(inventory_api_client):
    payload = {
        "product_id": 101,
        "quantity": 2
    }

    response = inventory_api_client.post("/inventory/check", payload)

    assert response.status_code == 200

    inventory = response.json()

    assert inventory["product_id"] == payload["product_id"]
    assert inventory["quantity"] == payload["quantity"]
    assert inventory["available"] is True
