from flask import current_app

db = current_app.db


class Token(db.Model):
    """
    """

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    token = db.Column(db.String(), nullable=False)
    expiry = db.Column(db.String(), nullable=False)
