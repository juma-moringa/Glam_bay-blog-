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
    blog = TextAreaField("Type Away:", validators=[Required()])
    submit = SubmitField("Post")

#comments form
class CommentsForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[Required()])
    name = StringField("Comment Name")
    submit = SubmitField("Comment")

#update blogs form
class UpdateBlogForm(FlaskForm):
    title = StringField("Blog title", validators=[Required()])
    blog = TextAreaField("Your blog", validators=[Required()])
    submit = SubmitField("Update")