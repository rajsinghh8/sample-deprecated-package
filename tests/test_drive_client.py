from unittest.mock import MagicMock, patch

from app.drive_client import build_authorized_http


def test_build_authorized_http_authorizes_with_loaded_credentials():
    fake_credentials = MagicMock()
    fake_authorized_http = MagicMock()
    fake_credentials.authorize.return_value = fake_authorized_http

    with patch(
        "app.drive_client.load_credentials", return_value=fake_credentials
    ) as mock_load:
        result = build_authorized_http("keyfile.json")

    mock_load.assert_called_once_with("keyfile.json")
    fake_credentials.authorize.assert_called_once()
    assert result is fake_authorized_http
