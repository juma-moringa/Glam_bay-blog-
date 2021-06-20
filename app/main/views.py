from flask import render_template, request, redirect, url_for
from . import main
from .. import db
from ..models import User, Comment, Blog, Subscriber
from flask_login import login_required, current_user
from datetime import datetime
from ..requests import get_quote
from ..email import mail_message
from .forms import BlogForm, CommentForm, UpdateBlogForm, UserProfile

# 1 the main index


@main.route("/", methods=["GET", "POST"])
def index():
    blogs = Blog.get_all_blogs()
    quote = get_quote()

    if request.method == "POST":
        new_sub = Subscriber(email=request.form.get("subscriber"))

        db.session.add(new_sub)
        db.session.commit()
        mail_message("Thank you for subscribing to Glam-bay blogs",
                     "email/welcome", new_sub.email)

    return render_template("index.html", blogs=blogs, quote=quote)


# 2 new log
@main.route("/blog/new", methods=["POST", "GET"])
@login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog_form.title.data = ""
        content = (blog_form.blog.data)
        blog_form.blog.data = ""
        # new_blog = Blog(title = title,content = content,posted = datetime.now(),blog_by = current_user.username, user_id = current_user.id)
        new_blog = Blog(title=title,
                        content=content,
                        posted=datetime.now(),
                        blog_by=current_user.username,
                        user_id=current_user.id)
        new_blog.save_blog()
        subs = Subscriber.query.all()
        for sub in subs:
            mail_message(title, "email/notification",
                         sub.email, new_blog=new_blog)
            pass
        return redirect(url_for("main.new_blog", id=new_blog.id))

    return render_template("new_blog.html", blog_form=blog_form)


# 3 create Commentblog
@main.route("/blog/<int:id>", methods=["POST", "GET"])
# def CommentBlog(id):
#     blog = Blog.query.filter_by(id=id).first()
#     comments = Comment.query.filter_by(blog_id=id).all()
#     comment_form = CommentForm()
#     comment_count = len(comments)

#     if comment_form.validate_on_submit():
#         comment = comment_form.comment.data
#         comment_form.comment.data = ""
#         comment_name = comment_form.name.data
#         comment_form.name.data = ""
#         if current_user.is_authenticated:
#             comment_name = current_user.username
#         new_comment = Comment(user= current_user, comment=comment, posted=datetime.now(), id=id)
#         new_comment.save_comment()
#         # return redirect(url_for("main.blog", id=blog.id))

#     return render_template("comments.html", blog = blog, comments=comments, comment_form=comment_form, comment_count=comment_count)

def CommentBlog(id):
    blog = Blog.query.filter_by(id = id).all()
    blogComments = Comment.query.filter_by(blog_id=id).all()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comment(blog_id=id, comment=comment, user=current_user)
        new_comment.save_comment()
    return render_template('comments.html', blog=blog, blog_comments=blogComments, comment_form=comment_form)


# 4 edit blog
# @main.route("/blog/<int:id>/update", methods=["POST", "GET"])
# @login_required
# def edit_blog(id):
#     blog = Blog.query.filter_by(id=id).first()
#     edit_form = UpdateBlogForm()

#     if edit_form.validate_on_submit():
#         blog.title = edit_form.title.data
#         edit_form.title.data = ""
#         blog.content = edit_form.blog.data
#         edit_form.blog.data = ""

#         db.session.add(blog)
#         db.session.commit()
#         return redirect(url_for("main.blog", id=blog.id))

#     return render_template("edit_blog.html", blog=blog, edit_form=edit_form)

@main.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_aBlog(id):
    blog = Blog.query.get_or_404(id)
    form = BlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.blog.data
        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        form.title.data = blog.title
        form.blog.data = blog.content
    return render_template('edit_ablog.html',blog=blog, form=form)


# 5 delete blog
@main.route('/deleteblog/<int:id>', methods=['GET', 'POST'])
@login_required

def delete_blog(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('main.index')) 

#6 update user profile
@main.route("/profile/<int:id>/update", methods = ["POST", "GET"])
@login_required
def update_profile(id):
    user = User.query.filter_by(id = id).first()
    form = UserProfile()
    if form.validate_on_submit():
        user.first_name = form.first_name.data
        # user.last_name = form.last_name.data
        user.email = form.email.data
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.profile", id = id))
    
    return render_template("profile/update.html",
                            user = user,
                            form = form)  

@main.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteComment(id):
    comment =Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    # flash('comment succesfully deleted')
    return redirect (url_for('main.index'))

# @main.route('/deleteblog/<int:id>', methods=['GET', 'POST'])
# @login_required
# def delete_blog(id):
#     blog =Blog.query.get_or_404(id)
#     db.session.delete(blog)
#     db.session.commit()
#     # flash('comment succesfully deleted')
#     return redirect (url_for('main.index'))


