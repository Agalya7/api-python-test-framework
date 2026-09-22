from fastapi import FastAPI

app = FastAPI()


@app.post("/payments")
def create_payment(payment: dict):
    return {
        "payment_id": 1,
        "order_id": payment["order_id"],
        "amount": payment["amount"],
        "status": "approved"
    }
