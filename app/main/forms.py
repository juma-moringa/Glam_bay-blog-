from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField)
from wtforms.validators import Required



class UserProfile(FlaskForm):
    first_name = StringField("First name...")
    email = StringField(" Your Email")
    last_name = StringField("Last Name...")
    bio = TextAreaField("Bio")
    submit = SubmitField("Update")

class BlogForm(FlaskForm):
    title = StringField("Blog title:", validators=[Required()])
    post = TextAreaField("Type Away:", validators=[Required()])
    submit = SubmitField("Post")

class CommentsForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[Required()])
    name = StringField("Comment Name")
    submit = SubmitField("Comment")


class UpdateBlogForm(FlaskForm):
    title = StringField("Blog title", validators=[Required()])
    blog = TextAreaField("Your blog", validators=[Required()])
    submit = SubmitField("Update")