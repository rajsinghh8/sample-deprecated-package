from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


def load_credentials(keyfile_path: str):
    """Load service-account credentials for calling Google APIs."""
    return ServiceAccountCredentials.from_json_keyfile_name(keyfile_path, SCOPES)


def is_expired(credentials) -> bool:
    return bool(credentials.access_token_expired)
