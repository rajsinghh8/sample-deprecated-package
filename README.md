# sample-deprecated-package

A minimal Flask app used to test VulnerabilityX's "package superseded" detection
and auto-migrate feature.

`requirements.txt` pins `Flask-Security==5.7.1`, which has a known open-redirect
vulnerability (GHSA-w2j7-f3c6-g8cw, fixed in 5.8.1). The app itself
(`app/__init__.py`, `app/models.py`, `app/routes.py`) uses the real
`flask_security` API (`Security`, `SQLAlchemyUserDatastore`, `UserMixin`,
`RoleMixin`, `login_required`, `roles_required`, `current_user`,
`hash_password`) — a real upgrade/migration needs to touch these files, not
just the dependency manifest.

`tests/test_routes.py` exercises the protected routes so the scan has
something real to verify before and after any change.
