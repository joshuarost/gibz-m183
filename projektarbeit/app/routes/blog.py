from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_required, current_user

from app.database.user import is_admin

blog_routes = Blueprint("blog_routes", __name__)


@blog_routes.route("/dashboard")
@login_required
def dashboard():
    if is_admin(current_user.username):
        return redirect(url_for("blog_routes.admin_dashboard"))
    return redirect(url_for("blog_routes.user_dashboard"))


@blog_routes.route("/user/dashboard")
@login_required
def user_dashboard():
    return render_template("dashboard.html")


@blog_routes.route("/admin/dashboard")
@login_required
def admin_dashboard():
    return render_template("dashboard.html")
