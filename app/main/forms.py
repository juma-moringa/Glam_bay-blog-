from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


# user profile form
class UserProfile(FlaskForm):
    first_name = StringField("Username")
    email = StringField(" Your Email")
    bio = TextAreaField("Bio")
    submit = SubmitField("Update")

# blog form
class BlogForm(FlaskForm):
    title = StringField("Blog title:", validators=[Required()])
    blog = TextAreaField("Write your blog:", validators=[Required()])
    submit = SubmitField("Blog")

#comments form
class CommentForm(FlaskForm):   
    name = StringField("Blog name")
    comment = TextAreaField(" Your Comment..", validators=[Required()])
    submit = SubmitField("Comment")

#update blogs form
class UpdateBlogForm(FlaskForm):
    title = StringField("Blog title", validators=[Required()])
    blog = TextAreaField("Your blog", validators=[Required()])
    submit = SubmitField("Update")