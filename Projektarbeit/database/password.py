"""
This modules implements functionalitys for save storing the password
"""

import bcrypt
import crypt

PEPPER = "$6$S9cvmZfrSawoXMJ4"

def hash(password, times=100000):
    """
    Hashes the given password with the given times or default
    """
    pass


def salt(password):
    """
    Creates a salt, stores it in the user and uses it on
    the provided password
    """
    salt = crypt.mksalt(crypt.METHOD_SHA512)
