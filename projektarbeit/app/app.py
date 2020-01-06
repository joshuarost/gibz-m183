from flask import Flask, Blueprint, current_app
from flask_login import LoginManager

from app.api.restplus import api
from app.routes.auth import auth_routes


def create_app():
    """Create flask app"""
    # app
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "m183_2fa"

    with app.app_context():
        pass

    # Database

    # Routes
    app.register_blueprint(auth_routes)

    # API
    blueprint = Blueprint("api", __name__, url_prefix="/api")
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
