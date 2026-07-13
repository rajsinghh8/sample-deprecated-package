# sample-deprecated-package

A minimal app used to test VulnerabilityX's "package superseded" detection and
auto-migrate feature.

`requirements.txt` pins `oauth2client==2.2.0`. Google officially deprecated
`oauth2client` years ago in favor of `google-auth` (+ `google-auth-oauthlib` /
`google-auth-httplib2` for the OAuth flow and httplib2 integration) — this is
a well-documented, real-world case, but `oauth2client` itself has no open CVE,
so VulnerabilityX won't pick it up as vulnerable on its own.

**To trigger the scan on this package**, use a version pin when starting the
run (e.g. tell the VulnerabilityX chat assistant "pin oauth2client to 4.1.3",
or pass `version_overrides: {"oauth2client": "4.1.3"}` to the run API) —
`resolve_upgrades` applies a requested version pin regardless of whether the
package is flagged as vulnerable, which is enough to put it through the same
upgrade → "is this superseded by a different package" check as a real CVE fix
would.

The app code (`app/google_auth_service.py`, `app/drive_client.py`) uses the
real `oauth2client` API (`ServiceAccountCredentials.from_json_keyfile_name`,
`.authorize()`, `.access_token_expired`) — migrating to `google-auth` needs a
genuinely different shape (`Credentials.from_service_account_file`,
`.expired`, `google_auth_httplib2.AuthorizedHttp`), not just a version bump in
the manifest. `tests/` mocks the credential objects so the suite runs without
real Google credentials, and should keep passing after a correct migration.
