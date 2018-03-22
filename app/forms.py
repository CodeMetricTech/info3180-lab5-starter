from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField,SelectField
from wtforms.validators import DataRequired, Email


class CreateUserForm(FlaskForm):
    firstname    = StringField('First Name', validators=[DataRequired()])
    lastname     = StringField('Last Name', validators=[DataRequired()])
    gender       = SelectField('Gender', validators=[DataRequired()] ,choices=[('Male','Male'),('Female','Female')])
    email        = StringField('Email', validators=[DataRequired(), Email()])
    location     = StringField('Location', validators=[DataRequired()])
    biography    = TextAreaField('Biography', validators=[DataRequired()])
    photo = FileField('Profile Picture',validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])