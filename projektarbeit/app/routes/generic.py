from flask import render_template, Blueprint, redirect, url_for, current_app as app
from flask_login import login_required, current_user

from app.database.user import is_admin

generic_routes = Blueprint("generic_routes", __name__)


@generic_routes.route("/")
def index():
    if current_user:
        return redirect(url_for("generic_routes.dashboard"))
    return render_template("login.html")


@generic_routes.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")
