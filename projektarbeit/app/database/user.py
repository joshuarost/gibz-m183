import bcrypt
from hashlib import sha256
from base64 import b64encode
from uuid import uuid4

from flask_login import UserMixin

from app.database.db import db

PEPPER = b"$6$S9cvmZfrSawoXMJ4"
MAX_ATTEMPTS = 3


class User(db.Model, UserMixin):
    """
    User class for the database including all requred fields
    """

    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    phonenumber = db.Column(db.String(), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Integer, nullable=False)
    attempts = db.Column(db.Integer, nullable=False)


def get_user_by_username(username):
    """
    Get the user with the provided username
    """
    return User.query.filter_by(username=username).first()


def get_user_by_id(userid):
    """
    Get the user with the provided username
    """
    return User.query.filter_by(id=userid).first()


def add_user(name, username, password, phonenumber, role=0, state=0):
    new_user = User(
        name=name,
        username=username,
        password=hash_password(password),
        phonenumber=phonenumber,
        role=role,
        state=state,
        attempts=0,
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user


def hash_password(password, rounds=15):
    """
    Hashes the given password with the given times or default
    """
    trimed = trim_and_pepper(password)

    # hash
    return bcrypt.hashpw(trimed, bcrypt.gensalt(rounds))


def trim_and_pepper(password):
    """
    Prepares the password for hashing and checking
    """
    # Pepper password
    pepperd = str.encode(password) + PEPPER

    # trim
    return b64encode(sha256(pepperd).digest())


def check_credentials(username, password):
    """
    Checks if username and password is correct

    Returns:
    """
    user = User.query.filter_by(username=username).first()
    if not user:
        return None, "Username does not exists"

    # check for blocked user
    if user.state == 1:
        return None, "This user has been previously blocked! Please ask an admin."

    trimed = trim_and_pepper(password)

    if bcrypt.checkpw(trimed, user.password):
        # success, remove attempts
        user.attempts = 0
        db.session.commit()

        return user, None

    # Wrong Credentials, increment attempts
    message = increment_attempts(username)
    return None, message


def increment_attempts(username):
    """
    Increments attempts and checks if user should be blocked
    """
    user = User.query.filter_by(username=username).first()
    user.attempts = user.attempts + 1

    if user.attempts >= MAX_ATTEMPTS:
        # User gets blocked
        user.attempts = 0
        user.state = 1
        db.session.commit()
        return "Your account has been blocked. Please contact an admin"

    db.session.commit()
    return "Passwort incorrect! You have {} attempts left.".format(
        MAX_ATTEMPTS - user.attempts
    )


def get_attempts(username):
    """
    Get the attempts of the provided user
    """
    user = User.query.filter_by(username=username).first()
    if user is None:
        return None
    return user.attempts


def is_admin(username):
    """
    Checks if prvided user is an admin
    """
    user = get_user_by_username(username)
    if user.role == 1:
        return True
    return False


def is_username_available(username):
    """
    Checks if the given username already exists
    """
    user = User.query.filter_by(username=username).first()
    if user is None:
        return True
    return False
