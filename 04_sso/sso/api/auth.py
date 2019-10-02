import base64
import os
from pathlib import Path
from io import BytesIO
import requests

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

import onetimepass
import pyqrcode
from google.oauth2 import id_token
from google.auth.transport import requests

auth_routes = Blueprint("auth_routes", __name__)

SECRET_FILE = Path("./.secret")
CREDENTIALS = {"username": "gipe", "password": "snowden"}
CLIENT_ID = "824399620081-0spurelgnenff5ncriber3np5ui0453i.apps.googleusercontent.com"


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
        if username == CREDENTIALS["username"] and password == CREDENTIALS["password"]:
            user = User(username)
            current_app.user = user
            login_user(user)
            return redirect(url_for("auth_routes.verify"))
        # wrong login
        flash("Wrong username or password")
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
        return render_template("verify.html", setup=not current_app.user.has_twofa())

    if request.method == "POST":
        current_app.user.set_otp_secret()
        token = request.form.get("token")
        if onetimepass.valid_totp(token, current_app.user.otp_secret):
            current_app.user.isverified = True
            return redirect(url_for("generic_routes.database"))
        return redirect(url_for("auth_routes.verify"))


@auth_routes.route("/qrcode")
def qrcode():
    """Returns qr code for 2fa if user is loged in"""
    if not current_app.user or current_app.user.has_twofa():
        return redirect(url_for("auth_routes.verify"))

    # render qrcode
    url = pyqrcode.create(current_app.user.get_totp_uri())
    stream = BytesIO()
    url.svg(stream, scale=3)
    return (
        stream.getvalue(),
        200,
        {
            "Content-Type": "image/svg+xml",
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
        },
    )


@auth_routes.route("/sso", methods=["POST"])
def sso():
    """
    Authenticates the google sso
    """
    token = request.get_data("idToken")

    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        userid = idinfo['sub']
        user = User(userid)
        user.isverified = True
        current_app.user = user
        login_user(user)
        return userid

    except ValueError:
        # Invalid token
        flash("Something went wrong with google")
        return None
