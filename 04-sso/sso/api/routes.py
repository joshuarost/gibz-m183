from flask import render_template, Blueprint, redirect, url_for, current_app
from flask_login import login_required

generic_routes = Blueprint("generic_routes", __name__)


@generic_routes.route("/")
def index():
    if current_app.user:
        return redirect(url_for("generic_routes.database"))
    return render_template("login.html")


@generic_routes.route("/database")
@login_required
def database():
    return render_template("database.html")
