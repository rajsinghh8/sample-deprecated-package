import pytest

from app import create_app


@pytest.fixture()
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as c:
        yield c


def test_dashboard_requires_login(client):
    resp = client.get("/dashboard", follow_redirects=False)
    assert resp.status_code in (302, 401)


def test_admin_requires_role(client):
    resp = client.get("/admin", follow_redirects=False)
    assert resp.status_code in (302, 401, 403)


def test_login_page_renders(client):
    resp = client.get("/login")
    assert resp.status_code == 200


def test_register_page_renders(client):
    resp = client.get("/register")
    assert resp.status_code == 200
