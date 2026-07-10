from src.api_client import ApiClient
from src.trip_service import TripService


# Test name doesn't describe the behavior under test; hits a real API client
# instead of mocking it.
def test_1():
    service = TripService(ApiClient())
    result = service.load_trips(42)
    assert result is not None