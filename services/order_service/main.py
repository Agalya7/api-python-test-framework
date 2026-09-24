import os

import requests
from fastapi import FastAPI

app = FastAPI()

PAYMENT_SERVICE_URL = os.getenv(
    "PAYMENT_SERVICE_URL",
    "http://127.0.0.1:8002"
)


@app.post("/orders")
def create_order(order: dict):
    payment = requests.post(
        f"{PAYMENT_SERVICE_URL}/payments",
        json={
            "order_id": 1,
            "amount": order["amount"]
        }
    )

    return {
        "order_id": 1,
        "product_id": order["product_id"],
        "quantity": order["quantity"],
        "status": "created",
        "payment_status": payment.json()["status"]
    }
