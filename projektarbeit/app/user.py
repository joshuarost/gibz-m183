import bcrypt
from hashlib import sha256

from app.database import db

PEPPER = b"$6$S9cvmZfrSawoXMJ4"


class User(db.Model):
    """
    User class for the database including all requred fields
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    phonenumber = db.Column(db.String(), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Integer, nullable=False)


def get_user(username):
    """
    Returns the user object or None if not found
    """
    return User.query.filter_by(username=username).first()


def hash_password(password, rounds=30):
    """
    Hashes the given password with the given times or default
    """
    trimed = sha256(password + PEPPER).digest()
    return bcrypt.hashpw(trimed, bcrypt.gensalt(rounds))


def check_credentials(username, password):
    user = User.query.filter_by(username=username).first()
    print(user)
    # return bcrypt.checkpw(password, hashed)

