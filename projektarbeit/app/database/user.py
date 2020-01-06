from flask import current_app

db = current_app.db


class User(db.Model):
    """
    User class for the database including all requred fields
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    salt = db.Column(db.String(), nullable=False)
    phonenumber = db.Column(db.String(), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Integer, nullable=False)


def create_default_user():
    """
    Creates a set of default user in the database
    Admin and User
    """
    pass


def get_user(username):
    """
    Returns the user object or None if not found
    """
    return User.query.filter_by(username=username).first()

