import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add project root to path

from Code.use_database import databaseManager

class testDatabase:
    def __init__(self):
        self.thisDatabase = databaseManager()
        self.connection = None

    def test_connection(self):
        con = self.thisDatabase.create_connection('../Code/test_database.db')
        self.connection = con
        try:
            assert self.connection is not None
            return "Connection test successful"
        except AssertionError:
            return "Connection test unsuccessful"

    def test_add_user(self):
        username = input("Enter a new username: ")
        password = input("Enter the user's password: ")
        role = input("Enter the user's role: ")
        team = input("Enter the user's team: ")
        row_id = self.thisDatabase.add_user(username, password, role, team)
        if row_id:
            print("User added successfully!")
            user_id = self.thisDatabase.get_last_row_id("users")
            thisUser = self.thisDatabase.find_user(user_id=user_id)
            if not thisUser:
                return "Cannot retrieve user - Add user test unsuccessful"
            try:
                assert thisUser[1] == username
                print("Username matches!")
            except AssertionError:
                return "Username doesn't match!"
            try:
                assert thisUser[3] == role
                print("User Role matches!")
            except AssertionError:
                return "User Role doesn't match!"
            try:
                assert thisUser[4] == team
                print("User Team matches!")
            except AssertionError:
                return "User Team doesn't match!"
            return "All subtests passed - Add user test successful"
        else:
            return "Cannot add user - Add user test unsuccessful"
        
    def test_add_project(self):
        project_title = input("Enter a new project title: ")
        project_details = input("Enter the project details: ")
        project_status = input("Enter the project status: ")
        project_review = input("Enter the project review status: ")
        project_owner = input("Enter the project owner (must be a registered user): ")
        row_id = self.thisDatabase.add_project(project_title, project_details, project_status, project_review, project_owner)
        if row_id:
            print("Project added successfully!")
            project_id = self.thisDatabase.get_last_row_id("projects")
            thisProject = self.thisDatabase.find_project(project_id=project_id)
            if not thisProject:
                return "Cannot retrieve project - Add project test unsuccessful"
            try:
                assert thisProject[1] == project_title
                print("Project title matches!")
            except AssertionError:
                return "Project title doesn't match!"
            try:
                assert thisProject[2] == project_details
                print("Project details match!")
            except AssertionError:
                return "Project details don't match!"
            try:
                assert thisProject[3] == project_status
                print("Project status matches!")
            except AssertionError:
                return "Project status doesn't match!"
            try:
                assert thisProject[4] == project_review
                print("Project review matches!")
            except AssertionError:
                return "Project review doesn't match!"
            try:
                assert thisProject[5] == project_owner
                print("Project owner matches!")
            except AssertionError:
                return "Project owner doesn't match!"
            return "All subtests passed - Add user test successful"
        else:
            return "Cannot add project - Add project test unsuccessful"

if __name__ == "__main__":
    thisTest = testDatabase()
    print(thisTest.test_connection())
    print(thisTest.test_add_user())
    print(thisTest.test_add_project())

        

    