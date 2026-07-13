from unittest.mock import MagicMock, patch

from app.google_auth_service import SCOPES, is_expired, load_credentials


def test_load_credentials_uses_expected_scopes():
    with patch(
        "google.oauth2.service_account.Credentials.from_service_account_file"
    ) as mock_load:
        mock_load.return_value = MagicMock()
        load_credentials("keyfile.json")
    mock_load.assert_called_once_with("keyfile.json", scopes=SCOPES)


def test_is_expired_reads_flag():
    creds = MagicMock()
    creds.valid = False
    assert is_expired(creds) is True

    creds.valid = True
    assert is_expired(creds) is False
