from flask import render_template, Blueprint, redirect, url_for, request
from flask_login import login_required, current_user

from app.routes.generic import admin_required
from app.database.user import is_admin
from app.database.comment import add_comment, get_all_comments_by_postid
from app.database.post import (
    get_posts_by_userid,
    get_all_posts,
    get_all_public_posts,
    get_post_by_id,
)

blog_routes = Blueprint("blog_routes", __name__)


@blog_routes.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    if is_admin(current_user.username):
        return redirect(url_for("blog_routes.admin_dashboard"))
    return redirect(url_for("blog_routes.user_dashboard"))


@blog_routes.route("/user/dashboard", methods=["GET"])
@login_required
def user_dashboard():
    posts = get_posts_by_userid(current_user.id)
    return render_template(
        "dashboard.html", posts=posts, is_admin=False, username=current_user.username
    )


@blog_routes.route("/admin/dashboard", methods=["GET"])
@login_required
@admin_required
def admin_dashboard():
    posts = get_all_posts()
    return render_template(
        "dashboard.html", posts=posts, is_admin=True, username=current_user.username
    )


@blog_routes.route("/home", methods=["GET"])
def home():
    posts = get_all_public_posts()
    return render_template("home.html", posts=posts)


@blog_routes.route("/post/<postid>", methods=["GET"])
def post(postid):
    post = get_post_by_id(postid)
    if post is None:
        return redirect(url_for("blog_routes.home"))

    # Get comments
    comments = get_all_comments_by_postid(postid)

    # Check if post is public
    if post.status == 0:
        return render_template(
            "post.html",
            post=post,
            comments=comments,
            is_loggedIn=current_user.is_authenticated,
        )
    return redirect(url_for("blog_routes.home"))


@blog_routes.route("/comment", methods=["POST"])
@login_required
def comment():
    userid = current_user.id
    postid = request.form.get("postid")
    comment = request.form.get("comment")

    if userid and postid and comment:
        comment = add_comment(userid, postid, comment)
    return redirect(url_for("blog_routes.post", postid=postid))
