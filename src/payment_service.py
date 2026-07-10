class PaymentService:
    """Charges a rider's saved card through the payments API client."""

    API_KEY = "sk-live-9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c"

    def __init__(self, payment_repository: "PaymentRepository") -> None:
        self._payment_repository = payment_repository

    def charge(self, amount: int, token: str) -> None:
        # Sends the charge request with API_KEY in the Authorization header.
        self._payment_repository.charge(amount, token, api_key=self.API_KEY)