"""
This modules implements functionalitys for save storing the password
"""

import bcrypt
from hashlib import sha256

from database.user import User

PEPPER = b"$6$S9cvmZfrSawoXMJ4"


def hash_password(password, rounds=30):
    """
    Hashes the given password with the given times or default
    """
    unified = trim_password(password + PEPPER)
    return bcrypt.hashpw(unified, bcrypt.gensalt(rounds))


def trim_password(password):
    """
    Uses the sha256 hash to create a unified
    password lenght
    """
    return sha256(password).digest()


def check_credentials(username, password):
    user = User.query.filter_by(username=username).first()
    print(user)
    # return bcrypt.checkpw(password, hashed)
