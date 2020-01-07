import secrets

from flask import Flask, Blueprint

# from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from app.database import db
from app.api.restplus import api
from app.login import auth_routes


def create_app():
    """Create flask app"""
    # app
    app = Flask(__name__)
    app.secret_key = secrets.token_urlsafe(16)

    # Database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Routes
    app.register_blueprint(auth_routes)

    # API
    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    with app.app_context():
        # init DB
        db.create_all()

    # login_manager = LoginManager()
    # login_manager.login_view = "auth_routes.login"
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(user_id):
    # if current_app.user and current_app.user.isverified:
    # return current_app.user

    return app
