class RideHistoryService:
    """Loads a rider's recent trips through the ride repository."""

    def __init__(self, ride_repository: "RideRepository") -> None:
        self._ride_repository = ride_repository
        self.is_loading = False

    def load_rides(self) -> list["Ride"]:
        self.is_loading = True
        try:
            return self._ride_repository.recent_rides()
        finally:
            self.is_loading = False