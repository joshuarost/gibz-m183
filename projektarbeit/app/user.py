import bcrypt
from hashlib import sha256
from base64 import b64encode

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


def add_user(name, username, password, phonenumber, role=0, state=0):
    new_user = User(
        name=name,
        username=username,
        password=hash_password(password),
        phonenumber=phonenumber,
        role=role,
        state=state,
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

    Returns: bool:
        True: if success full
        False: if username or password wrong
    """
    user = User.query.filter_by(username=username).first()
    if not user:
        return None

    trimed = trim_and_pepper(password)

    if bcrypt.checkpw(trimed, user.password):
        return user
    return None
