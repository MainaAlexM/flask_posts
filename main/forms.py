from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import TextAreaField, StringField, SelectField, SubmitField

class PitchForm(FlaskForm):

    title = StringField('Title',validators=[Required()])
    text = TextAreaField('Your Pitch',validators=[Required()])
    category = SelectField('Type',choices=[('Business','Business pitch'),('Team','Team pitch'),('Love','Love pitch')],validators=[Required()])
    submit = SubmitField('Post Pitch')


class CommentForm(FlaskForm):
    text = TextAreaField('Comment:',validators=[Required()])
    submit = SubmitField('Post Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [Required()])
    submit = SubmitField('Update')