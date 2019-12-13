from flask import Flask, Blueprint, current_app
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from api.restplus import api
from api import BLUEPRINTS
from api.auth import User


def create_app():
    """Create flask app"""
    # app
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "m183_Projektarbeit"

    # db
    with app.app_context():
        app.user = None
        app.db = SQLAlchemy(app)

    # API
    blueprint = Blueprint("api", __name__, url_prefix="/")
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    login_manager = LoginManager()
    login_manager.login_view = "auth_routes.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        if current_app.user and current_app.user.isverified:
            return current_app.user

    return app
