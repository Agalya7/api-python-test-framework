from fastapi import FastAPI

app = FastAPI()


@app.post("/orders")
def create_order(order: dict):
    return {
        "order_id": 1,
        "product_id": order["product_id"],
        "quantity": order["quantity"],
        "status": "created"
    }
