from api.routes import generic_routes
from api.auth import auth_routes

BLUEPRINTS = [
    generic_routes,
    auth_routes]

# expose blueprints
__all__ = ["BLUEPRINTS"]
