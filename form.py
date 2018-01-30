from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.fields import DateField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid e-mail!'), Length(max=50)])

class TodoForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(max=50)], render_kw={"placeholder": "Create a new task"})
    description = StringField('Description', validators=[InputRequired(), Length(max=200)])
    priority = SelectField('Priority', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    deadline = DateField('Deadline', format='%m/%d/%Y', render_kw={"placeholder": "MM/DD/YYYY"})