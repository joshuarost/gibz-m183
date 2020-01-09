from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_required, current_user

from app.database.user import is_admin

generic_routes = Blueprint("generic_routes", __name__)


@generic_routes.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("blog_routes.dashboard"))
    # return render_template("login.html")
    return redirect(url_for("blog_routes.home"))
