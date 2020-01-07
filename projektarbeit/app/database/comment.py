from flask import current_app

db = current_app.db


class Comment(db.Model):
    """
    """

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    title = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(), nullable=False)
