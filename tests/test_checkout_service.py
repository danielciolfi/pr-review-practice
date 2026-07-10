from src.api_client import ApiClient
from src.checkout_service import CheckoutService


# Hits the real API client instead of mocking it.
def test_checkout():
    service = CheckoutService(ApiClient())
    service.SubmitOrder(1)