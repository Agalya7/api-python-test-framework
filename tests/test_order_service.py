import requests


BASE_URL = "http://127.0.0.1:8001"


def test_create_order():
    payload = {
        "product_id": 101,
        "quantity": 2
    }

    response = requests.post(
        f"{BASE_URL}/orders",
        json=payload
    )

    assert response.status_code == 200

    order = response.json()

    assert order["order_id"] == 1
    assert order["product_id"] == 101
    assert order["quantity"] == 2
    assert order["status"] == "created"
