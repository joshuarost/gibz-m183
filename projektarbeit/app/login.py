import base64
import os
from pathlib import Path
from io import BytesIO

from flask import (
    render_template,
    Blueprint,
    request,
    redirect,
    url_for,
    flash,
    current_app,
    abort,
)
from flask_login import UserMixin, login_user, logout_user

from base64 import b64encode

from app.user import User, check_credentials, add_user
from app.token import set_token, check_token
from app.api.sms import send_token

auth_routes = Blueprint("auth_routes", __name__)

SECRET_FILE = Path("./.secret")
CREDENTIALS = {"username": "gipe", "password": "snowden"}


class User(UserMixin):
    """User"""

    def __init__(self, username):
        super()
        self.id = username
        self.otp_secret = base64.b32encode(os.urandom(10)).decode("utf-8")
        self.isverified = False

    def get_totp_uri(self):
        """Returns totp uri"""
        return "otpauth://totp/M183-2FA:{0}?secret={1}&issuer=M183-2FA".format(
            self.id, self.otp_secret
        )

    def has_twofa(self):
        """indicates if 2fa file exists"""
        return SECRET_FILE.is_file()

    def set_otp_secret(self):
        """Sets the otp secret"""
        if self.has_twofa():
            with open(str(SECRET_FILE), "r") as reader:
                self.otp_secret = reader.readline()
        else:
            with open(str(SECRET_FILE), "w") as writer:
                writer.write(self.otp_secret)


@auth_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = check_credentials(username, password)
        if user:
            token = send_token(user.phonenumber)
            set_token(user.id, token)
            current_app.user = user
            return redirect(url_for("auth_routes.verify"))
            # user = User(username)
            # login_user(user)
        # wrong login
        flash("Wrong username or password")
        return redirect(url_for("auth_routes.login"))


@auth_routes.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        phonenumber = request.form.get("phonenumber")

        if name and username and password and phonenumber:
            user = add_user(name, username, password, phonenumber)
            print(user)
            return redirect(url_for("auth_routes.login"))


@auth_routes.route("/logout", methods=["GET"])
def logout():
    """Logouts the current user"""
    current_app.user = None
    return redirect(url_for("generic_routes.index"))


@auth_routes.route("/verify", methods=["GET", "POST"])
def verify():
    """Verifys the given token with the local one"""
    if request.method == "GET":
        if not current_app.user:
            return redirect(url_for("generic_routes.index"))
        return render_template("verify.html")

    if request.method == "POST":
        token = request.form.get("token")
        result = check_token(current_app.user.id, token)
        print(result)

