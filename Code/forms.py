from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add project root to path

from Code.use_database import databaseManager
import os

thisDatabase = databaseManager()
thisDatabase.create_connection(os.path.join(os.getcwd(), 'Code/database.db'))

def validate_project_owner(form, field):
    thisUser = thisDatabase.find_user(username=field.data)
    if not thisUser:
        print('User does not exist')
        raise ValidationError('User does not exist')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()], render_kw={"type": "password"})
    submit = SubmitField('Submit')

class PasswordResetForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()], render_kw={"type": "password"})
    confirm_password = StringField('Confirm Password', validators=[DataRequired()], render_kw={"type": "password"})
    submit = SubmitField('Submit')

class CreateUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()], render_kw={"type": "password"})
    role = SelectField('Role', choices=[('User', 'User'), ('Supervisor', 'Supervisor'), ('Admin', 'Admin')], validators=[DataRequired()])
    team = SelectField('Team', choices=[('Police', 'Police'), ('Intern', 'Intern'), ('Other', 'Other')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateUserDetailsForm(FlaskForm):
    users = [(user[1], user[1]) for user in thisDatabase.get_all_from_table('users')]
    username = SelectField('Username', choices=users, validators=[DataRequired()])
    password = StringField('Password', render_kw={"type": "password"})
    role = SelectField('Role', choices=[('User', 'User'), ('Supervisor', 'Supervisor'), ('Admin', 'Admin')])
    team = SelectField('Team', choices=[('Police', 'Police'), ('Intern', 'Intern'), ('Other', 'Other')])
    submit = SubmitField('Submit')

class UsersInProjectsForm(FlaskForm):
    users = [(user[1], user[1]) for user in thisDatabase.get_all_from_table('users')]
    projects = [(project[1], project[1]) for project in thisDatabase.get_all_from_table('projects')]
    project_title = SelectField('Project Title', choices=projects, validators=[DataRequired()])
    username = SelectMultipleField('Username', choices=users, validators=[DataRequired()])
    submit = SubmitField('Submit')

class RemoveProjectUsersForm(FlaskForm):
    projects = [(project[1], project[1]) for project in thisDatabase.get_all_from_table('projects')]
    project_title = SelectField('Project Title', choices=projects, validators=[DataRequired()])
    
    # This will be populated dynamically via JavaScript after selecting a project
    username = SelectMultipleField('Users to Remove', validators=[DataRequired()])
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
    task_title = StringField('Task Title')
    task_details = TextAreaField('Task Details')
    task_status = SelectField('Task Status', choices=[('In Progress', 'In Progress'), ('Complete', 'Complete'), ('New', 'New'), ('Overdue', 'Overdue')])
    task_assigned_date = StringField('Task Assigned Date', render_kw={"type": "date"})
    task_due_date = StringField('Task Due Date', render_kw={"type": "date"})
    submit = SubmitField('Submit')

class EditProjectForm(FlaskForm):
    project_id = StringField('Project ID', validators=[DataRequired()])
    projet_title = StringField('Project Title')
    project_details = TextAreaField('Project Details')
    project_status = SelectField('Project Status', choices=[('In Progress', 'In Progress'), ('Complete', 'Complete'), ('Other', 'Other')])
    project_review = SelectField('Project Review', choices=[
        ('1 day', '1 day'),
        ('3 days', '3 days'),
        ('1 week', '1 week'),
        ('2 weeks', '2 weeks'),
        ('1 month', '1 month')])
    users = [(user[1], user[1]) for user in thisDatabase.get_all_from_table('users')]
    project_owner = SelectField('Project Owner', choices=users)
    submit = SubmitField('Submit')
