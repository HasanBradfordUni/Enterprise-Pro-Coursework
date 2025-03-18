import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add project root to path

from Code.use_database import databaseManager
import datetime

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
            return "All subtests passed - Add project test successful"
        else:
<<<<<<< HEAD
            return "Cannot add project - Add project test unsuccessful"

if __name__ == "__main__":
    thisTest = testDatabase()
    print(thisTest.test_connection())
    print(thisTest.test_add_user())
    print(thisTest.test_add_project())

=======
            return "Cannot add project - Add project test unsuccessful"  
>>>>>>> 3e51d50 (writing more tests for adding to database, all tables now complete)
        
    def test_add_task(self):
        task_title = input("Enter a new task title: ")
        task_details = input("Enter the task details: ")
        task_status = input("Enter the task status: ")
        task_assigned_date = input("Enter the task assigned date (DD/MM/YYYY format): ")
        date1 = task_assigned_date.split('/')
        year1 = date1[2]
        month1 = date1[1]
        day1 = date1[0]
        task_assigned_date = datetime.datetime(year=year1, month=month1, day=day1)
        task_due_date = input("Enter the task due date (DD/MM/YYYY format): ")
        date2 = task_assigned_date.split('/')
        year2 = date2[2]
        month2 = date2[1]
        day2 = date2[0]
        task_due_date = datetime.datetime(year=year2, month=month2, day=day2)
        project_id = int(input("Enter the project id: "))
        row_id = self.thisDatabase.add_task(task_title, task_details, task_status, task_assigned_date, task_due_date, project_id)
        if row_id:
            print("Task added successfully!")
            task_id = self.thisDatabase.get_last_row_id("tasks")
            thisTask = self.thisDatabase.find_task(task_id=task_id)
            if not thisTask:
                return "Cannot retrieve task - Add task test unsuccessful"
            try:
                assert thisTask[1] == task_title
                print("Task title matches!")
            except AssertionError:
                return "Task title doesn't match!"
            try:
                assert thisTask[2] == task_details
                print("Task details match!")
            except AssertionError:
                return "Task details don't match!"
            try:
                assert thisTask[3] == task_status
                print("Task status matches!")
            except AssertionError:
                return "Task status doesn't match!"
            try:
                assert thisTask[4] == task_assigned_date
                print("Task assigned date matches!")
            except AssertionError:
                return "Task assigned date doesn't match!"
            try:
                assert thisTask[5] == task_due_date
                print("Task due date matches!")
            except AssertionError:
                return "Task due date doesn't match!"
            try:
                assert thisTask[6] == project_id
                print("Project id matches!")
            except AssertionError:
                return "Project id doesn't match!"    
            return "All subtests passed - Add task test successful"
        else:
            return "Cannot add task - Add task test unsuccessful"
            
    def test_add_user_into_project(self):
        project_title = input("Enter a new project title: ")
        user_id = int(input("Enter user id: "))
        username = input("Enter a new user name: ")
        project_id = int(input("Enter the project id: "))
        row_id = self.thisDatabase.add_user_into_project(project_id, project_title, user_id, username)
        if row_id:
            print("User added successfully!")
            project_user_id = self.thisDatabase.get_last_row_id("project_users")
            thisUserinProject = self.thisDatabase.find_user_in_project(project_user_id=project_user_id)
            if not thisUserinProject:
                return "Cannot retrieve user in project - Add user into project test unsuccessful"
            try:
                assert thisUserinProject[2] == project_title
                print("Project title matches!")
            except AssertionError:
                return "Project title doesn't match!"
            try:
                assert thisUserinProject[3] == user_id
                print("User id matches!")
            except AssertionError:
                return "User id doesn't match!"
            try:
                assert thisUserinProject[4] == username
                print("Username matches!")
            except AssertionError:
                return "Username doesn't match!"
            try:
                assert thisUserinProject[1] == project_id
                print("Project id matches!")
            except AssertionError:
                return "Project id doesn't match!"    
            return "All subtests passed - Add user into project test successful"
        else:
            return "Cannot add user into project- Add user into project test unsuccessful"
                        
    def test_add_assigned_task(self):
        task_id = int(input("Enter task id"))
        task_title = input("Enter a new task title: ")
        assigned_user_id = int(input("Enter user id: "))
        assigned_username = input("Enter user name: ")
        project_id = int(input("Enter the project id: "))
        row_id = self.thisDatabase.add_user_into_project(task_id, task_title, assigned_user_id, assigned_username, project_id)
        if row_id:
            print("Assigned task added successfully!")
            assigned_tasks_id = self.thisDatabase.get_last_row_id("assigned_tasks")
            thisAssignedTask = self.thisDatabase.find_assigned_task(assigned_task_id=assigned_tasks_id)
            if not thisAssignedTask:
                return "Cannot retrieve assigned task - Add assigned task test unsuccessful"
            try:
                assert thisAssignedTask[2] == task_title
                print("Task title matches!")
            except AssertionError:
                return "Task title doesn't match!"
            try:
                assert thisAssignedTask[1] == task_id
                print("Task id matches!")
            except AssertionError:
                return "Task id doesn't match!"
            try:
                assert thisAssignedTask[3] == assigned_user_id
                print("Assigned user id matches!")
            except AssertionError:
                return "Assigned user id doesn't match!"
            try:
                assert thisAssignedTask[4] == assigned_username
                print("Assigned username matches!")
            except AssertionError:
                return "Assigned username doesn't match!"
            try:
                assert thisAssignedTask[5] == project_id
                print("Project id matches!")
            except AssertionError:
                return "Project id doesn't match!"    
            return "All subtests passed - Add assigned task test successful"
        else:
            return "Cannot add assigned task- Add assigned task test unsuccessful"
        
    def test_add_task_update(self):
        project_id = int(input("Enter the project id: "))
        print("Do you wish to test progress update or task status update?")
        print("1. Progress update")
        print("2. Task Status update")
        choice = input("Enter 1 or 2 to choose from the options above: ")
        if choice == "1":
            progress_update = input("Enter the progress update to the current project: ")
            row_id = self.thisDatabase.add_task_update(project_id=project_id, progress_update=progress_update)
            if row_id:
                print("Task update added successfully!")
                task_updates_id = self.thisDatabase.get_last_row_id("task_updates")
                thisTaskUpdate = self.thisDatabase.find_task_update(task_update_id=task_updates_id)
                if not thisTaskUpdate:
                    return "Cannot retrieve Task update - Add Task update test unsuccessful"
                try:
                    assert thisTaskUpdate[2] == progress_update
                    print("Task Progress update matches!")
                except AssertionError:
                    return "Task Progress update doesn't match!"
                try:
                    assert thisTaskUpdate[1] == project_id
                    print("Project id matches!")
                except AssertionError:
                    return "Project id doesn't match!"    
                return "All subtests passed - Add Task update test successful"
            else:
                return "Cannot add Task update- Add Task update test unsuccessful"
        elif choice == "2":
            task_status = input("Enter the new task status: ")
            row_id = self.thisDatabase.add_task_update(project_id=project_id, new_status=task_status)
            if row_id:
                print("Task update added successfully!")
                task_updates_id = self.thisDatabase.get_last_row_id("task_updates")
                thisTaskUpdate = self.thisDatabase.find_task_update(task_update_id=task_updates_id)
                if not thisTaskUpdate:
                    return "Cannot retrieve Task update - Add Task update test unsuccessful"
                try:
                    assert thisTaskUpdate[3] == task_status
                    print("Task update status matches!")
                except AssertionError:
                    return "Task update status doesn't match!"
                try:
                    assert thisTaskUpdate[1] == project_id
                    print("Project id matches!")
                except AssertionError:
                    return "Project id doesn't match!"    
                return "All subtests passed - Add Task update test successful"
            else:
                return "Cannot add Task update - Add Task update test unsuccessful"

        
        
            
            