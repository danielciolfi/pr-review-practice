class ApiClient:
    """Thin wrapper around the team's shared HTTP client."""

    def get(self, path: str) -> dict:
        ...

    def post(self, path: str, payload: dict) -> dict:
        ...