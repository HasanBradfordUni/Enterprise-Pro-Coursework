import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add project root to path

from Code.use_database import databaseManager
from datetime import datetime

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

    def test_update_project(self):
        project_id = int(input("Enter the project id of the project you wish to update: "))
        title = ""
        details = ""
        status = ""
        review = ""
        owner = ""
        title_update = input("Do you wish to update the project title (y/n)? ")
        if title_update.upper() == "Y":
            title = input("Enter the new project title: ") 
        details_update = input("Do you wish to update the project details (y/n)? ")
        if details_update.upper() == "Y":
            details = input("Enter the new project details: ")
        status_update = input("Do you wish to update the project status (y/n)? ")
        if status_update.upper() == "Y":
            status = input("Enter the new project status: ")
        review_update = input("Do you wish to update the project review (y/n)? ")
        if review_update.upper() == "Y":
            review = input("Enter the new project review: ")
        owner_update = input("Do you wish to update the project owner (y/n)? ")
        if owner_update.upper() == "Y":
            owner = input("Enter the new project owner: ")
        row_id = self.thisDatabase.update_project(project_id, title, details, status, review, owner)
        if row_id:
            print("Project updated successfully!")
            thisProject = self.thisDatabase.find_project(project_id=project_id)
            if not thisProject:
                return "Cannot retrieve project - Update project test unsuccessful"
            try:
                if title == "":
                    print("Project title wasn't updated!")
                else:
                    assert thisProject[1] == title
                    print("Project title matches!")
            except AssertionError:
                return "Project title doesn't match!"
            try:
                if details == "":
                    print("Project details wasn't updated!")
                else:
                    assert thisProject[2] == details
                    print("Project details match!")
            except AssertionError:
                return "Project details don't match!"
            try:
                if status == "":
                    print("Project status wasn't updated!")
                else:
                    assert thisProject[3] == status
                    print("Project status matches!")
            except AssertionError:
                return "Project status doesn't match!"
            try:
                if review == "":
                    print("Project review wasn't updated!")
                else:
                    assert thisProject[4] == review
                    print("Project review matches!")
            except AssertionError:
                return "Project review doesn't match!"
            try:
                if owner == "":
                    print("Project owner wasn't updated!")
                else:
                    assert thisProject[5] == owner
                    print("Project owner matches!")
            except AssertionError:
                return "Project owner doesn't match!"
            return "All subtests passed - Update project test successful"
        else:
            return "Cannot update project - Update project test unsuccessful"
        
    def test_update_task(self):
        task_id = int(input("Enter the task id of the task you wish to update: "))
        title = ""
        details = ""
        status = ""
        assigned_date = ""
        due_date = ""
        project_id = 0
        title_update = input("Do you wish to update the task title (y/n)? ")
        if title_update.upper() == "Y":
            title = input("Enter the new task title: ") 
        details_update = input("Do you wish to update the task details (y/n)? ")
        if details_update.upper() == "Y":
            details = input("Enter the new task details: ")
        status_update = input("Do you wish to update the task status (y/n)? ")
        if status_update.upper() == "Y":
            status = input("Enter the new task status: ")
        assigned_date_update = input("Do you wish to update the task assigned date (y/n)? ")
        if assigned_date_update.upper() == "Y":
            assigned_date = input("Enter the new task assigned date: ")
        due_date_update = input("Do you wish to update the task due date (y/n)? ")
        if due_date_update.upper() == "Y":
            due_date = input("Enter the new task due date: ")
        project_id_update = input("Do you wish to update the project id (y/n)? ")
        if project_id_update.upper() == "Y":
            project_id = int(input("Enter the new project id: ")) 
        row_id = self.thisDatabase.update_task(task_id, title, details, status, assigned_date, due_date, project_id)
        if row_id:
            print("Task updated successfully!")
            thisTask = self.thisDatabase.find_task(task_id=task_id)
            if not thisTask:
                return "Cannot retrieve task - Update task test unsuccessful"
            try:
                if title == "":
                    print("Task title wasn't updated!")
                else:
                    assert thisTask[1] == title
                    print("Task title matches!")
            except AssertionError:
                return "Task title doesn't match!"
            try:
                if details == "":
                    print("Task details wasn't updated!")
                else:
                    assert thisTask[2] == details
                    print("Task details match!")
            except AssertionError:
                return "Task details don't match!"
            try:
                if status == "":
                    print("Task status wasn't updated!")
                else:
                    assert thisTask[3] == status
                    print("Task status matches!")
            except AssertionError:
                return "Task status doesn't match!"
            try:
                if assigned_date == "":
                    print("Task assigned date wasn't updated!")
                else:
                    assert thisTask[4] == assigned_date
                    print("Task assigned date matches!")
            except AssertionError:
                return "Task assigned date doesn't match!"
            try:
                if due_date == "":
                    print("Task due date wasn't updated!")
                else:
                    assert thisTask[5] == due_date
                    print("Task due date matches!")
            except AssertionError:
                return "Task due date doesn't match!"
            try:
                if project_id == 0:
                    print("Project id wasn't updated!")
                else:
                    assert thisTask[6] == project_id
                    print("Project id matches!")
            except AssertionError:
                return "Project id doesn't match!"
            return "All subtests passed - Update task test successful"
        else:
            return "Cannot update task - Update task test unsuccessful"       
        
    def test_update_user_in_project(self):
        project_user_id = int(input("Enter the project user id of the user in project you wish to update: "))
        project_id = int(input("Enter the project id of the project you wish to update: "))
        title = ""
        user_id = int(input("Enter the user id of the user you wish to update"))
        username = ""
        title_update = input("Do you wish to update the project title (y/n)? ")
        if title_update.upper() == "Y":
            title = input("Enter the new project title: ") 
        username_update = input("Do you wish to update the username (y/n)? ")
        if username_update.upper() == "Y":
            username = input("Enter the new username: ")
        row_id = self.thisDatabase.update_user_in_project(project_user_id, project_id, title, user_id, username)
        if row_id:
            print("User in project updated successfully!")
            thisProject = self.thisDatabase.find_project(project_id=project_id)
            if not thisProject:
                return "Cannot retrieve project - Update user in project test unsuccessful"
            try:
                if title == "":
                    print("Project title wasn't updated!")
                else:
                    assert thisProject[2] == title
                    print("Project title matches!")
            except AssertionError:
                return "Project title doesn't match!"
            try:
                if username == "":
                    print("Username wasn't updated!")
                else:
                    assert thisProject[4] == username
                    print("Username matches!")
            except AssertionError:
                return "Username don't match!"
            return "All subtests passed - Update user in project test successful"
        else:
            return "Cannot update user in project - Update user in project test unsuccessful"
        
    def test_update_assigned_task(self):
        assigned_task_id = int(input("Enter the assigned task id of the assigned task you wish to update: "))
        task_id = 0
        task_title = ""
        user_id = 0
        username = ""
        project_id = 0
        task_id_update = input("Do you wish to update the task id (y/n)? ")
        if task_id_update.upper() == "Y":
            task_id = int(input("Enter the new task id: "))
        task_title_update = input("Do you wish to update the task title (y/n)? ")
        if task_title_update.upper() == "Y":
            task_title = input("Enter the new task title: ")
        user_id_update = input("Do you wish to update the assigned user's id (y/n)? ")
        if user_id_update.upper() == "Y":
            user_id = input("Enter the new user id: ")
        username_update = input("Do you wish to update the assigned user's username (y/n)? ")
        if username_update.upper() == "Y":
            username = input("Enter the new username: ")
        project_id_update = input("Do you wish to update the project id of the assigned task (y/n)? ")
        if project_id_update.upper() == "Y":
            project_id = int(input("Enter the new project id: "))
        row_id = self.thisDatabase.update_assigned_task(assigned_task_id, task_id, task_title, user_id, username, project_id)
        if row_id:
            print("Assigned task updated successfully!")
            thisTask = self.thisDatabase.find_assigned_task(assigned_task_id=assigned_task_id)
            if not thisTask:
                return "Cannot retrieve task - Update assigned task test unsuccessful"
            try:
                if task_id == 0:
                    print("Task id wasn't updated!")
                else:
                    assert thisTask[1] == task_id
                    print("Task id matches!")
            except AssertionError:
                return "Task id doesn't match!"
            try:
                if task_title == "":
                    print("Task title wasn't updated!")
                else:
                    assert thisTask[2] == task_title
                    print("Task title matches!")
            except AssertionError:
                return "Task title doesn't match!"
            try:
                if user_id == 0:
                    print("Assigned user's id wasn't updated!")
                else:
                    assert thisTask[3] == user_id
                    print("Assigned user's id matches!")
            except AssertionError:
                return "Assigned user's id doesn't match!"
            try:
                if username == "":
                    print("Assigned user's username wasn't updated!")
                else:
                    assert thisTask[4] == username
                    print("Assigned username matches!")
            except AssertionError:
                return "Assigned user's username doesn't match!"
            try:
                if project_id == "":
                    print("Assigned task's project id wasn't updated!")
                else:
                    assert thisTask[5] == project_id
                    print("Project id matches!")
            except AssertionError:
                return "Assigned task's project id doesn't match!"
            return "All subtests passed - Update assigned task test successful"
        else:
            return "Cannot update task - Update assigned task test unsuccessful"
        
    def test_delete_user(self):
        users = self.thisDatabase.get_all_from_table("users")
        user_ids = []
        usernames = []
        while user_identifier not in user_ids or user_identifier not in usernames:
            for user in users:
                print(f"User id: {user[0]}; Username: {user[1]}")
                user_ids.append(user[0])
                usernames.append(user[1])
            user_identifier = input("Enter the user id or username of the user you wish to delete: ")
            if user_identifier not in user_ids or user_identifier not in usernames:
                print("Error! Please enter a valid username/id from the list above")
        try:
            user_id = 0
            username = ""
            if user_identifier.isdigit():
                user_id = user_identifier
            else:
                username = user_identifier
            row_id = self.thisDatabase.delete_user(user_id=user_id, username=username)
            assert row_id is not None
            return f"User with identifier {user_identifier} deleted successfully - Delete user test successful"
        except AssertionError:
            return f"User with identifier {user_identifier} could not be deleted - Delete user test unsuccessful"
           
    def test_delete_project(self):
        projects = self.thisDatabase.get_all_from_table("projects")
        project_ids = []
        while project_identifier not in project_ids:
            for project in projects:
                print(f"Project id: {project[0]}")
                project_ids.append(project[0])
            project_identifier = input("Enter the project id of the project you wish to delete: ")
            if project_identifier not in project_ids:
                print("Error! Please enter a valid project id from the list above")
        try:
            project_id = 0
            row_id = self.thisDatabase.delete_project(project_id=project_id)
            assert row_id is not None
            return f"Project with identifier {project_identifier} deleted successfully - Delete project test successful"
        except AssertionError:
            return f"Project with identifier {project_identifier} could not be deleted - Delete project test unsuccessful"
        
    def test_delete_task(self):
        tasks = self.thisDatabase.get_all_from_table("tasks")
        task_ids = []
        task_titles = []
        project_ids = []
        while task_identifier not in task_ids or task_identifier not in task_titles:
            for task in tasks:
                print(f"Task id: {task[0]}; Task title: {task[1]}; Project id: {task[2]}")
                task_ids.append(task[0])
                task_titles.append(task[1])
                project_ids.append(task[2])
            task_identifier = input("Enter the task id or task title for the task you wish to delete: ")
            if task_identifier not in task_ids or task_identifier not in task_titles:
                print("Error! Please enter a valid task title or task/project id from the list above")
        try:
            task_id = 0
            task_title = ""
            project_id = 0
            if task_identifier.isdigit():
                task_id = task_identifier
            else:
                task_title = task_identifier
                project_id =  int(input("Enter the project id for the task you wish to delete: "))
            row_id = self.thisDatabase.delete_task(task_id=task_id, task_title=task_title, project_id=project_id)
            assert row_id is not None
            return f"Task with identifier {task_identifier} deleted successfully - Delete task test sucessful"
        except AssertionError:
            return f"Task with identifier {task_identifier} could not be deleted - Delete task test unsucessful"
           
    def test_delete_project_user(self):
        project_users = []
        unique_ids = []
        project_ids = []
        user_ids = []
        usernames = []
        project_users = self.thisDatabase.get_all_from_table("project_users")
        for project_user in project_users:
            print(f"Unique id: {project_user[0]}; Project id: {project_user[1]}; User id: {project_user[3]}; Username: {project_user[4]}")
            unique_ids.append(project_user[0])
            project_ids.append(project_user[1])
            user_ids.append(project_user[3])
            usernames.append(project_user[4])
        print("Do you wish to delete via unique id or project id and user details?")
        print("1. Unique id")
        print("2. Project id and User details")
        choice = input("Enter 1 or 2 to choose from the options above: ")
        if choice == "1":
            unique_id = input("Enter the unique id of the user in project you wish to delete: ")
            row_id = self.thisDatabase.remove_user_from_project(project_user_id=unique_id)
            try:
                assert row_id is not None
                return f"User in project with identifier {unique_id} deleted successfully - Delete project user test sucessful"
            except AssertionError:
                return f"User in project with identifier {unique_id} could not be deleted - Delete project user test unsucessful"
        elif choice == "2":
            project_id = 0
            user_id = 0
            username = ""
            while project_id not in project_ids:
                project_id = input("Enter the project id of the user in project you wish to delete: ")
                if project_id not in project_ids:
                    print("Error! Please enter a valid project id from the list above")
            while user_identifier not in user_ids or user_identifier not in usernames:
                user_identifier = input("Enter the user id or username of the user in project you wish to delete: ")
                if user_identifier not in user_ids or user_identifier not in usernames:
                    print("Error! Please enter a valid username/id from the list above")
            if user_identifier.isdigit():
                user_id = user_identifier
            else:
                username = user_identifier
            row_id = self.thisDatabase.remove_user_from_project(project_id=project_id, user_id=user_id, username=username)
            try:
                assert row_id is not None
                return f"User in project with project id {project_id} and user identifier {user_identifier} deleted successfully - Delete project user test sucessful"
            except AssertionError:
                return f"User in project with project id {project_id} and user identifier {user_identifier} could not be deleted - Delete project user test unsucessful"
           
    def test_delete_assigned_task(self):
        assigned_tasks = []
        unique_ids = []
        project_ids = []
        user_ids = []
        task_ids = []
        assigned_tasks = self.thisDatabase.get_all_from_table("assigned_tasks")
        for assigned_task in assigned_tasks:
            print(f"Unique id: {assigned_task[0]}; Project id: {assigned_task[5]}; User id: {assigned_task[3]}; Task id: {assigned_task[1]}")
            unique_ids.append(assigned_tasks[0])
            project_ids.append(assigned_tasks[5])
            user_ids.append(assigned_tasks[3])
            task_ids.append(assigned_tasks[1])
        print("Do you wish to delete via unique id or project id and user id and task id?")
        print("1. Unique id")
        print("2. Project id and User id and Task id")
        choice = input("Enter 1 or 2 to choose from the options above: ")
        if choice == "1":
            unique_id = input("Enter the unique id of the user in project you wish to delete: ")
            row_id = self.thisDatabase.remove_assigned_task(assigned_task_id=unique_id)
            try:
                assert row_id is not None
                return f"Assigned Task with identifier {unique_id} deleted successfully - Delete assigned task test sucessful"
            except AssertionError:
                return f"Assigned Task with identifier {unique_id} could not be deleted - Delete assigned task test unsucessful"
        elif choice == "2":
            project_id = 0
            user_id = 0
            task_id = 0
            while project_id not in project_ids:
                project_id = input("Enter the project id of the user in project you wish to delete: ")
                if project_id not in project_ids:
                    print("Error! Please enter a valid project id from the list above")
            while user_id not in user_ids:
                user_id = input("Enter the user id of the user in project you wish to delete: ")
                if user_id not in user_ids:
                    print("Error! Please enter a valid user id from the list above")
            while task_id not in task_ids:
                task_id = input("Enter the task id of the user in project you wish to delete: ")
                if task_id not in task_ids:
                    print("Error! Please enter a valid task id from the list above")
            row_id = self.thisDatabase.remove_assigned_task(task_id=task_id, user_id=user_id, project_id=project_id)
            try:
                assert row_id is not None
                return f"Assigned Task with project id {project_id} and user id {user_id} and task id {task_id} deleted successfully - Delete assigned task test sucessful"
            except AssertionError:
                return f"User in project with project id {project_id} and user id {user_id} and task id {task_id} could not be deleted - Delete assigned task test unsucessful"
                   