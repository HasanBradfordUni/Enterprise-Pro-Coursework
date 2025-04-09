# Testing/conftest.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add project root to path

import pytest
from Code.app import app, myObj
from Code.use_database import databaseManager
from Code.search_sort import listOperationsManager

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

@pytest.fixture
def db():
    db = databaseManager()
    db.create_connection(':memory:')  # Use in-memory DB for tests
    yield db
    db.connection.close()

def test_add_user(db):
    row_id = db.add_user("test_user", "pass", "user", "team")
    assert row_id is not None
    user = db.find_user(username="test_user")
    assert user[1] == "test_user"

def test_add_project(db):
    db.add_user("owner", "pass", "admin", "team")
    row_id = db.add_project("Project", "Details", "Status", "Review", "owner")
    assert row_id is not None
    project = db.find_project(project_title="Project")
    assert project[1] == "Project"

def test_merge_sort():
    manager = listOperationsManager()
    tasks = ["Write report", "Review code", "Fix bugs"]
    sorted_tasks = manager.merge_sort(tasks.copy())
    assert sorted_tasks == sorted(tasks)

def clear_all_tables(self):
    tables = ['users', 'projects', 'tasks']
    for table in tables:
        self.connection.execute(f"DELETE FROM {table}")
    self.connection.commit()