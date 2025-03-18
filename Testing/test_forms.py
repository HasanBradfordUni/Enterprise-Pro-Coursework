import sys
import os

# Get the parent directory (project-root)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
code_dir = os.path.join(project_root, "Code")

# Add to Python path
sys.path.insert(0, code_dir)

from forms import CreateProjectForm, CreateUserForm, LoginForm, UpdateUserDetailsForm, UsersInProjectsForm
import pytest

sys.path.clear()
sys.path.insert(0, os.path.abspath(__file__))

def test_login_form_validation():
    # Test DataRequired validators
    form = LoginForm(data={})
    assert not form.validate()
    assert 'Username' in form.errors
    assert 'Password' in form.errors

    # Test valid submission
    form = LoginForm(data={'username': 'test', 'password': 'pass'})
    assert form.validate()

def test_create_project_owner_validation(monkeypatch):
    # Mock database response for project owner validation
    def mock_find_user(username):
        return True if username == "valid_user" else None

    monkeypatch.setattr('forms.thisDatabase.find_user', mock_find_user)

    # Test invalid owner
    form = CreateProjectForm(
        data={'project_owner': 'invalid_user', 'project_title': 'Test'}
    )
    assert not form.validate()
    assert 'User does not exist' in form.project_owner.errors

    # Test valid owner
    form = CreateProjectForm(
        data={'project_owner': 'valid_user', 'project_title': 'Test'}
    )
    assert form.validate()

def test_update_user_details_choices(monkeypatch):
    # Mock database response for dynamic username choices
    mock_users = [('1', 'user1'), ('2', 'user2')]
    monkeypatch.setattr(
        'forms.thisDatabase.get_all_from_table',
        lambda _: mock_users
    )

    form = UpdateUserDetailsForm()
    assert form.username.choices == [('user1', 'user1'), ('user2', 'user2')]

test_login_form_validation()
test_create_project_owner_validation()
test_update_user_details_choices()