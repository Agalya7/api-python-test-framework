from pathlib import Path

import pytest
from pact import Pact, match

from services.order_service import main as order_service


@pytest.fixture
def pact():
    pact = Pact("order-service", "payment-service").with_specification("V4")
    yield pact
    pact.write_file(Path(__file__).parent / "pacts")


def test_order_service_payment_contract(pact):
    (
        pact.upon_receiving("A request to create a payment")
        .with_request("POST", "/payments")
        .with_body(
            {
                "order_id": 1,
                "amount": 49.99
            },
            content_type="application/json",
            part="Request"
        )
        .will_respond_with(200)
        .with_body(
            {
                "payment_id": match.int(1),
                "order_id": match.int(1),
                "amount": match.decimal(49.99),
                "status": match.str("approved")
            },
            content_type="application/json"
        )
    )

    with pact.serve() as mock_server:
        order_service.PAYMENT_SERVICE_URL = str(mock_server.url)

        order = order_service.create_order({
            "product_id": 101,
            "quantity": 2,
            "amount": 49.99
        })

        assert order["payment_status"] == "approved"
