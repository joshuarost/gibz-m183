from flask import (
    render_template,
    Blueprint,
    request,
    redirect,
    url_for,
    flash,
    current_app as app,
)
from flask_login import login_user, logout_user

from app.database.user import (
    check_credentials,
    add_user,
    get_user_by_username,
    is_username_available,
)
from app.database.token import set_token, check_token, send_token, delete_token

auth_routes = Blueprint("auth_routes", __name__)


@auth_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user, message = check_credentials(username, password)
        if user is None:
            # wrong login
            flash(message)
            return redirect(url_for("auth_routes.login"))

        token = send_token(user.phonenumber)
        set_token(user.id, token)
        app.username = user.username
        return redirect(url_for("auth_routes.verify"))


@auth_routes.route("/verify", methods=["GET", "POST"])
def verify():
    """Verifys the given token with the local one"""
    if request.method == "GET":
        if not app.username:
            return redirect(url_for("generic_routes.index"))
        return render_template("verify.html")

    if request.method == "POST":
        token = request.form.get("token")
        if check_token(app.username, token):
            login_user(get_user_by_username(app.username))
            delete_token(app.username)

            # remove user from session
            app.username = None
            return redirect(url_for("blog_routes.dashboard"))

        return redirect(url_for("auth_routes.verify"))


@auth_routes.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("username")
        name = request.form.get("name")
        password = request.form.get("password")
        phonenumber = request.form.get("phonenumber")

        if name and username and password and phonenumber:
            if not is_username_available(username):
                flash("Username is already in user!")
                return redirect(url_for("auth_routes.register"))

            # Add user
            user = add_user(name, username, password, phonenumber)
            return redirect(url_for("auth_routes.login"))

        return redirect(url_for("auth_routes.register"))


@auth_routes.route("/logout", methods=["GET"])
def logout():
    """Logouts the current user"""
    logout_user()
    return redirect(url_for("auth_routes.login"))
