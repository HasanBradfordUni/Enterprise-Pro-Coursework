# test_forms.py
import sys
import os
import pytest
from flask import Flask

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import after setting up path
from Code.forms import CreateProjectForm, CreateUserForm, LoginForm, UpdateUserDetailsForm

@pytest.fixture(scope='module')
def app():
    # Create test Flask app
    app = Flask(__name__)
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SECRET_KEY'] = 'test-secret-key'
    
    with app.app_context():
        yield app

def test_login_form_validation(app):
    with app.test_request_context():
        # Test DataRequired validators
        form = LoginForm(data={})
        assert not form.validate()
        assert 'Username' in form.errors
        assert 'Password' in form.errors

        # Test valid submission
        form = LoginForm(data={'username': 'test', 'password': 'pass'})
        assert form.validate()

def test_create_project_owner_validation(app, monkeypatch):
    with app.test_request_context():
        # Mock database response
        def mock_find_user(username):
            return True if username == "valid_user" else None

        from Code import forms
        monkeypatch.setattr(forms.thisDatabase, 'find_user', mock_find_user)

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

def test_update_user_details_choices(app, monkeypatch):
    with app.test_request_context():
        # Mock database response
        mock_users = [('1', 'user1'), ('2', 'user2')]
        
        from Code import forms
        monkeypatch.setattr(
            forms.thisDatabase,
            'get_all_from_table',
            lambda _: mock_users
        )

        form = UpdateUserDetailsForm()
        assert form.username.choices == [('user1', 'user1'), ('user2', 'user2')]