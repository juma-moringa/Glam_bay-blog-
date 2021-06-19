from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField)
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField("Blog title:", validators=[Required()])
    post = TextAreaField("Type Away:", validators=[Required()])
    submit = SubmitField("Post")