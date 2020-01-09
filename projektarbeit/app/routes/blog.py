from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_required, current_user

from app.database.user import is_admin
from app.database.post import get_posts_by_userid, get_all_posts, get_all_public_posts, get_post_by_id

blog_routes = Blueprint("blog_routes", __name__)


@blog_routes.route("/dashboard")
@login_required
def dashboard():
    if is_admin(current_user.username):
        return redirect(url_for("blog_routes.admin_dashboard"))
    return redirect(url_for("blog_routes.user_dashboard"))


@blog_routes.route("/user/dashboard")
@login_required
def user_dashboard():
    posts = get_posts_by_userid(current_user.id)
    return render_template("dashboard.html", posts = posts, is_admin=False, username=current_user.username)


@blog_routes.route("/admin/dashboard")
@login_required
def admin_dashboard():
    posts = get_all_posts()
    return render_template("dashboard.html", posts = posts, is_admin=True, username=current_user.username)


@blog_routes.route("/home")
def home():
    posts = get_all_public_posts()
    return render_template("home.html", posts = posts)


@blog_routes.route("/post/<postid>")
def post(postid):
    post = get_post_by_id(postid)

    # Check if post is public
    if post.status == 0:
        return render_template("post.html", post = post)
    return redirect(url_for("blog_routes.home"))
