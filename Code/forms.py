from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()], render_kw={"type": "password"})
    submit = SubmitField('Submit')

class CreateUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()], render_kw={"type": "password"})
    role = StringField('Role', validators=[DataRequired()])
    team = StringField('Team', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateUserDetailsForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()], render_kw={"type": "password"})
    role = StringField('Role', validators=[DataRequired()])
    team = StringField('Team', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CreateProjectForm(FlaskForm):
    project_title = StringField('Project Title', validators=[DataRequired()])
    project_details = StringField('Project Details', validators=[DataRequired()])
    project_status = StringField('Project Status', validators=[DataRequired()])
    project_review = StringField('Project Review', validators=[DataRequired()])
    project_owner = StringField('Project Owner', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UpdateProgressForm(FlaskForm):
    progress_update = StringField('Progress Update', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditTaskForm(FlaskForm):
    task_id = StringField('Task ID', validators=[DataRequired()])
    task_title = StringField('Task Title', validators=[DataRequired()])
    task_details = StringField('Task Details', validators=[DataRequired()])
    task_status = StringField('Task Status', validators=[DataRequired()])
    task_assigned_date = StringField('Task Assigned Date', validators=[DataRequired()])
    task_due_date= StringField('Task Due Date', validators=[DataRequired()])
    submit = SubmitField('Submit')
