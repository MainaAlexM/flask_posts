from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField

class PitchForm(FlaskForm):
    content = TextAreaField('New Pitch')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment_section_id = TextAreaField('New Comment')
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    name = TextAreaField('Category')
    submit = SubmitField()