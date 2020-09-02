from http import HTTPStatus

from app.api.restplus import api
from flask_restplus import Resource

from app.database.post import get_all_public_posts

ns = api.namespace("posts", description="Post operations")


def post_to_json(post):
    """
    Coverts the given post to a json object
    """
    return {
        "userid": post.userid,
        "title": post.title,
        "content": post.content,
        "status": post.status,
    }


@ns.route("")
class Posts(Resource):
    @ns.response(HTTPStatus.OK, "Successfully fetched posts")
    def get(self):
        """
        Return all the public post
        """
        posts = []
        # conver to json
        for post in get_all_public_posts():
            posts.append(post_to_json(post))

        return posts, HTTPStatus.OK
