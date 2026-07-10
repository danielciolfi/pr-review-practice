class TripService:
    def __init__(self, api_client):
        self.api_client = api_client

    def load_trips(self, user_id):
        # Calls the API client directly instead of going through a repository.
        return self.api_client.get(f"/users/{user_id}/trips")