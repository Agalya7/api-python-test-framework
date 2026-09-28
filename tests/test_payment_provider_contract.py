from pathlib import Path

from pact import Verifier


def test_payment_service_provider_contract():
    verifier = (
        Verifier("payment-service")
        .add_source(
            Path(__file__).parent / "pacts"
        )
        .add_transport(
            url="http://localhost:8002"
        )
    )

    verifier.verify()
