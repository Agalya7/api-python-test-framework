from fastapi import FastAPI

app = FastAPI()


@app.post("/inventory/check")
def check_inventory(item: dict):
    return {
        "product_id": item["product_id"],
        "quantity": item["quantity"],
        "available": True
    }
