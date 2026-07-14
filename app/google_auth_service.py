from google.oauth2 import service_account
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


def load_credentials(keyfile_path: str):
    """Load service-account credentials for calling Google APIs."""
    return service_account.Credentials.from_service_account_file(
        keyfile_path, scopes=SCOPES
    )


def is_expired(credentials) -> bool:
    return not credentials.valid
