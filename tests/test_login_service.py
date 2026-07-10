from unittest.mock import Mock

import pytest

from src.login_service import LoginService


@pytest.fixture
def auth_repository() -> Mock:
    return Mock()


def test_log_in_calls_auth_repository_with_credentials(auth_repository: Mock) -> None:
    service = LoginService(auth_repository)

    service.log_in("user@example.com", "hunter2")

    auth_repository.sign_in.assert_called_once_with("user@example.com", "hunter2")
    assert service.is_loading is False


def test_log_in_sets_error_message_on_failure(auth_repository: Mock) -> None:
    auth_repository.sign_in.side_effect = ValueError("invalid credentials")
    service = LoginService(auth_repository)

    service.log_in("user@example.com", "wrong")

    assert service.error_message == "invalid credentials"