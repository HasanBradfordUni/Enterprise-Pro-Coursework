# Testing/tests/test_routes.py
import pytest
from flask import url_for, session

# Test Authentication Workflow
def test_unauthenticated_access(client):
    # Test redirect to login when not authenticated
    routes = ['/', '/admin', '/supervisor', '/tasks']
    for route in routes:
        response = client.get(route, follow_redirects=False)
        assert response.status_code == 302
        assert '/login' in response.location

# Test Login Route
def test_login_route(client):
    # GET request
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Log in to the YHROCU' in response.data

    # POST with invalid credentials
    response = client.post('/login', data={
        'username': 'invalid',
        'password': 'wrong'
    }, follow_redirects=True)
    assert b'User does not exist' in response.data

    # POST with valid credentials (replace with real test user)
    response = client.post('/login', data={
        'username': 'test_admin',
        'password': 'admin_pass'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Configure admin settings' in response.data  # Verify redirect

# Test Admin Routes
def test_admin_routes(client):
    # First log in
    client.post('/login', data={
        'username': 'test_admin',
        'password': 'admin_pass'
    })
    
    # Test admin dashboard
    response = client.get('/admin')
    assert response.status_code == 200
    assert b'Create Project' in response.data
    assert b'Create User' in response.data

    # Test user creation
    response = client.post('/create_user', data={
        'username': 'new_user',
        'password': 'temp_pass',
        'role': 'User',
        'team': 'Police'
    }, follow_redirects=True)
    assert b'User added successfully' in response.data

# Test Project Management
def test_project_workflow(client):
    client.post('/login', data={'username': 'test_admin', 'password': 'admin_pass'})
    
    # Create project
    response = client.post('/create_project', data={
        'project_title': 'Test Project',
        'project_details': 'Test Details',
        'project_status': 'In Progress',
        'project_review': '1 week',
        'project_owner': 'test_admin'
    }, follow_redirects=True)
    assert b'Project added successfully' in response.data

    # Delete project
    response = client.get('/delete_project/1', follow_redirects=True)
    assert response.status_code == 200

# Test Task Management
def test_task_workflow(client):
    client.post('/login', data={'username': 'test_user', 'password': 'user_pass'})
    
    # Create task
    response = client.post('/create_task', data={
        'task-title': 'Test Task',
        'task-details': 'Task Details',
        'task-due-date': '2024-12-31'
    }, follow_redirects=True)
    assert b'Test Task' in response.data

    # Delete task
    response = client.get('/delete_task/1', follow_redirects=True)
    assert response.status_code == 200

# Test Logout
def test_logout(client):
    client.post('/login', data={'username': 'test_user', 'password': 'user_pass'})
    response = client.get('/logout', follow_redirects=True)
    assert myObj.user_logged_in == False
    assert b'Login' in response.data