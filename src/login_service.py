class LoginService:
    """Authenticates a user through the auth repository."""

    def __init__(self, auth_repository: "AuthRepository") -> None:
        self._auth_repository = auth_repository
        self.is_loading = False
        self.error_message: str | None = None

    def log_in(self, email: str, password: str) -> None:
        self.is_loading = True
        try:
            self._auth_repository.sign_in(email, password)
        except Exception as exc:
            self.error_message = str(exc)
        finally:
            self.is_loading = False