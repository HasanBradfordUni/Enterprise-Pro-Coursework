# Testing/tests/conftest.py
import pytest
from Code.app import app, myObj

@pytest.fixture(scope='module')
def client():
    # Configure test settings
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    
    # Reset app state before tests
    myObj.user_logged_in = False
    myObj.user_id = 0
    myObj.user_role = "user"
    
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def cleanup_db(client):
    yield
    # Clear test database after tests
    if app.config['TESTING']:
        with app.app_context():
            myObj.database.clear_all_tables()