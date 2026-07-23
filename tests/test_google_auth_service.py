from unittest.mock import MagicMock, patch

from app.google_auth_service import SCOPES, is_expired, load_credentials


def test_load_credentials_uses_expected_scopes():
    with patch(
        "app.google_auth_service.ServiceAccountCredentials.from_json_keyfile_name"
    ) as mock_load:
        mock_load.return_value = MagicMock()
        load_credentials("keyfile.json")
    mock_load.assert_called_once_with("keyfile.json", SCOPES)


def test_is_expired_reads_flag():
    creds = MagicMock()
    creds.access_token_expired = True
    assert is_expired(creds) is True

    creds.access_token_expired = False
    assert is_expired(creds) is False
