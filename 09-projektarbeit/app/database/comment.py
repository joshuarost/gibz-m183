from uuid import uuid4

from app.database.db import db
from app.database.user import get_user_by_id


class Comment(db.Model):
    """
    Comment of a post
    """

    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid4()))
    userid = db.Column(db.String(), nullable=False)
    postid = db.Column(db.String(), nullable=False)
    comment = db.Column(db.String(), nullable=False)


def add_comment(userid, postid, comment):
    """
    Add new comment with the given information
    """
    new_comment = Comment(userid=userid, postid=postid, comment=comment)
    db.session.add(new_comment)
    db.session.commit()
    return new_comment


def get_all_comments_by_postid(postid):
    """
    Get all the comments for a post by id
    """
    comments = Comment.query.filter_by(postid=postid).all()

    # replace userid with the username for showing
    for comment in comments:
        comment.userid = get_user_by_id(comment.userid).username
    return comments
