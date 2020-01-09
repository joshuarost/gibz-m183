import secrets

from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_talisman import Talisman

from app.database.db import db
from app.api.restplus import api
from app.database.user import get_user_by_id
from app.routes.auth import auth_routes
from app.routes.generic import generic_routes
from app.routes.blog import blog_routes


def create_app():
    """Create flask app"""
    # app
    app = Flask(__name__)
    app.secret_key = secrets.token_urlsafe(16)

    # setup XSS and Clickjacking security
    csp = {'default-src': '\'self\''}
    Talisman(app, content_security_policy={}, force_https=False)

    # Database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Routes
    app.register_blueprint(auth_routes)
    app.register_blueprint(generic_routes)
    app.register_blueprint(blog_routes)

    # API
    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    with app.app_context():
        # init DB
        db.create_all()
        app.username = None

    # Create login manager
    login_manager = LoginManager()
    login_manager.login_view = "auth_routes.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(userid):
        print(userid)
        return get_user_by_id(userid)

    return app
