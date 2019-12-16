
from flask import current_app

db = current_app.db


class Comment(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True)
    postid = db.Column(db.Integer)
    userid = db.Column(db.Integer)
    title = db.Column(db.String(), nullable=False)
    comment = db.Column(db.String(), nullable=False)
