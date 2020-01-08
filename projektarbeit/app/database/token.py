import requests
from datetime import datetime
from base64 import b64encode
from http import HTTPStatus

from app.database.db import db
from app.database.user import get_user_by_username

EXPIRATION = 300  # 5 minutes in seconds
SMS_URL = "https://europe-west1-gibz-informatik.cloudfunctions.net/send_2fa_sms"


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    token = db.Column(db.String(), nullable=False)
    creation = db.Column(db.DateTime, nullable=False)


def set_token(userid, token):
    """
    Set the token for the given user
    """
    old_token = Token.query.filter_by(userid=userid).first()

    if old_token is None:
        return add_toke(userid, token)

    # update existing token
    old_token.token = token
    old_token.creation = datetime.now()
    db.session.commit()
    return old_token


def add_toke(userid, token):
    """
    Adds a new token to the db
    """
    new_token = Token(userid=userid, token=token, creation=datetime.now())
    db.session.add(new_token)
    db.session.commit()
    return new_token


def check_token(username, token):
    """
    Checkts if the token is still valid and matches
    """
    userid = get_user_by_username(username).id
    saved_token = Token.query.filter_by(userid=userid).first()
    if saved_token is None:
        return False

    if (datetime.now() - saved_token.creation).seconds > 300:
        return False
    return saved_token.token == token


def send_token(phonenumber, length=6, flash=False):
    """
    """
    header = {
        "Authorization": b64encode("19_20.M183.jrost".encode("utf-8")),
        "Content-Type": "application/json",
    }

    body = {"recipient": phonenumber, "length": length, "flash": flash}

    result = requests.post(SMS_URL, headers=header, json=body)

    if result.status_code == HTTPStatus.OK:
        return result.json()["token"]
    return None


def delete_token(username):
    """
    Delete if existing the token of the provided user

    nothing happens if the token does not exist because
    the same effect as deleting has occurd
    """
    userid = get_user_by_username(username).id
    saved_token = Token.query.filter_by(userid=userid).first()

    if saved_token:
        db.session.delete(saved_token)
        db.session.commit()
