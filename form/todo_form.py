from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.fields import DateField
from wtforms.validators import InputRequired, Length

class TodoForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(max=50)], render_kw={"placeholder": "Create a new task"})
    description = StringField('Description', validators=[InputRequired(), Length(max=200)])
    priority = SelectField('Priority', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    deadline = DateField('Deadline', format='%m/%d/%Y', render_kw={"placeholder": "MM/DD/YYYY"})