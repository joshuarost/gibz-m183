"""
This modules implements functionalitys for save storing the password
"""

import bcrypt
from hashlib import sha256

PEPPER = b"$6$S9cvmZfrSawoXMJ4"


def hash(password, rounds=25):
    """
    Hashes the given password with the given times or default
    """
    unified = trim(password + PEPPER)
    return bcrypt.hashpw(unified, bcrypt.gensalt(rounds))


def trim(password):
    """
    Uses the sha256 hash to create a unified
    password lenght
    """
    return sha256(password).digest()
