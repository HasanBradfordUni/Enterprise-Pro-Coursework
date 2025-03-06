from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from use_database import databaseManager

thisDatabase = databaseManager()

def validate_project_owner(field):
    thisUser = thisDatabase.find_user(field.data)
    if not thisUser:
        raise ValidationError('User does not exist')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()], render_kw={"type": "password"})
    submit = SubmitField('Submit')

class CreateUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()], render_kw={"type": "password"})
    role = SelectField('Role', choices=[('User', 'User'), ('Supervisor', 'Supervisor'), ('Admin', 'Admin')], validators=[DataRequired()])
    team = SelectField('Team', choices=[('Police', 'Police'), ('Intern', 'Intern'), ('Other', 'Other')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateUserDetailsForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()], render_kw={"type": "password"})
    role = SelectField('Role', choices=[('User', 'User'), ('Supervisor', 'Supervisor'), ('Admin', 'Admin')], validators=[DataRequired()])
    team = SelectField('Team', choices=[('Police', 'Police'), ('Intern', 'Intern'), ('Other', 'Other')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class CreateProjectForm(FlaskForm):
    project_title = StringField('Project Title', validators=[DataRequired()])
    project_details = TextAreaField('Project Details', validators=[DataRequired()])
    project_status = SelectField('Project Status', choices=[('In Progress', 'In Progress'), ('Complete', 'Complete'), ('Other', 'Other')], validators=[DataRequired()])
    project_review = SelectField('Project Review', choices=[
        ('1 day', '1 day'),
        ('3 days', '3 days'),
        ('1 week', '1 week'),
        ('2 weeks', '2 weeks'),
        ('1 month', '1 month')
    ], validators=[DataRequired()])
    project_owner = StringField('Project Owner', validators=[DataRequired(), validate_project_owner])
    submit = SubmitField('Submit')

class UpdateProgressForm(FlaskForm):
    progress_update = StringField('Progress Update', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditTaskForm(FlaskForm):
    task_id = StringField('Task ID', validators=[DataRequired()])
    task_title = StringField('Task Title', validators=[DataRequired()])
    task_details = TextAreaField('Task Details', validators=[DataRequired()])
    task_status = SelectField('Task Status', choices=[('In Progress', 'In Progress'), ('Complete', 'Complete'), ('New', 'New'), ('Overdue', 'Overdue')], validators=[DataRequired()])
    task_assigned_date = StringField('Task Assigned Date', validators=[DataRequired()], render_kw={"type": "date"})
    task_due_date = StringField('Task Due Date', validators=[DataRequired()], render_kw={"type": "date"})
    submit = SubmitField('Submit')
