from uuid import uuid4

from app.database.db import db


class Post(db.Model):
    """
    Post of a user can make
    """
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid4()))
    userid = db.Column(db.String(), nullable=False )
    title = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)
    status = db.Column(db.Integer, nullable=False)


def add_post(userid, title, content, status=0):
    """
    Add new post with the given information
    """
    new_post = Post(
        userid=userid,
        title=title,
        content=content,
        status=status,
    )
    db.session.add(new_post)
    db.session.commit()
    return new_post


def get_posts_by_userid(userid):
    """
    Returns all post of the given user which are not deleted
    """
    return Post.query.filter_by(userid=userid, status=0).all()


def get_all_posts():
    """
    Returns all posts
    """
    return Post.query.all()
