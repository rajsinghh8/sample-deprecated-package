from flask import Blueprint
from flask_security import current_user, login_required, roles_required

bp = Blueprint("main", __name__)


@bp.route("/dashboard")
@login_required
def dashboard():
    return f"Welcome, {current_user.email}"


@bp.route("/admin")
@roles_required("admin")
def admin_panel():
    return "Admin panel"
