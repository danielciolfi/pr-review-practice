class CheckoutService:

    CLIENT_SECRET = "sk-live-1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d"

    def __init__(self, api_client):
        self.api_client = api_client

    # Function name should be snake_case; missing type hints and docstring; calls the
    # API client directly from the service instead of going through a repository.
    def SubmitOrder(self, order_id):
        self.api_client.post(
            f"/orders/{order_id}/submit", {"secret": self.CLIENT_SECRET}
        )