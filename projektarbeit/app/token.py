from datetime import datetime

from app.database import db

EXPIRATION = 300 # 5 minutes in seconds


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
    new_token = Token(
        userid=userid,
        token=token,
        creation=datetime.now()
    )
    db.session.add(new_token)
    db.session.commit()
    return new_token


def check_token(userid, token):
    """
    Checkts if the token is still valid and matches
    """
    saved_token = Token.query.filter_by(userid=userid).first()
    if saved_token is None:
        return False

    if (datetime.now() - saved_token.creation).seconds > 300:
        return False
    return saved_token == token


