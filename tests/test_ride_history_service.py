from unittest.mock import Mock

from src.ride_history_service import RideHistoryService


def test_load_rides_returns_recent_rides_from_repository() -> None:
    ride_repository = Mock()
    ride_repository.recent_rides.return_value = ["ride-1", "ride-2"]
    service = RideHistoryService(ride_repository)

    rides = service.load_rides()

    assert rides == ["ride-1", "ride-2"]
    assert service.is_loading is False