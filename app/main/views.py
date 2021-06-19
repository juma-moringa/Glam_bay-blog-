from flask import (render_template, request, redirect, url_for)
from . import main
from .. import db
from ..models import User, Comment, Blog, Subscribers
from flask_login import login_required, current_user
from .forms import (UpdateProfile, PostForm,CommentForm, UpdatePostForm)
from datetime import datetime
from ..request import get_quote
from ..email import mail_message

@main.route("/", methods = ["GET", "POST"])
def index():
    blogs = Blog.get_all_blogs()
    quote = get_quote()

    if request.method == "POST":
        new_sub = Subscribers(email = request.form.get("subscriber"))
        db.session.add(new_sub)
        db.session.commit()
        mail_message("Thank you for subscribing to Glam-bay blogs","email/welcome", new_sub.email)
    return render_template("index.html",blogs = blogs,quote = quote)