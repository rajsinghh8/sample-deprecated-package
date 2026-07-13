import httplib2

from app.google_auth_service import load_credentials


def build_authorized_http(keyfile_path: str) -> httplib2.Http:
    """Return an httplib2.Http instance authorized to call Google Drive."""
    credentials = load_credentials(keyfile_path)
    return credentials.authorize(httplib2.Http())
