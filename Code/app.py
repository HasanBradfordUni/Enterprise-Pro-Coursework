from flask import Flask, request, jsonify, render_template, Blueprint, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

from use_database import databaseManager
from search_sort import listOperationsManager
from forms import LoginForm, CreateUserForm, UpdateUserDetailsForm, CreateProjectForm, UpdateProgressForm
from forms import EditTaskForm, UsersInProjectsForm, PasswordResetForm, RemoveProjectUsersForm, EditProjectForm, RemoveAssignedUsersForm
 
class myClass():
    def __init__(self, router):
        self.blueprint = Blueprint('myClass', __name__)
        self.user_logged_in = False
        self.deleted_tasks = []
        self.deleted_projects = []
        router('/')(self.index)
        router('/supervisor')(self.supervisor)
        router('/tasks')(self.tasks)
        router('/create_task', methods=['POST'])(self.create_task)
        router('/sort_tasks', methods=['GET', 'POST'])(self.sort_tasks)
        router('/filter_tasks', methods=['GET', 'POST'])(self.filter_tasks)
        router('/update_progress', methods=['GET', 'POST'])(self.update_progress)
        router('/edit_task', methods=['GET', 'POST'])(self.edit_task)
        router('/delete_task', methods=['GET', 'POST'])(self.delete_task)
        router('/show_deleted_tasks')(self.show_deleted_tasks)
        router('/assign_users', methods=['POST'])(self.assign_users)
        router('/search_tasks/<string:search_term>')(self.search_tasks)
        router('/login', methods=['GET', 'POST'])(self.login)
        router('/search_projects/<string:search_term>')(self.search_projects)
        router('/filter_projects/<string:filter_type>/<string:filter_word>')(self.filter_projects)
        router('/sort_projects/<string:sort_type>')(self.sort_projects)
        router('/add_user_to_project', methods=['GET', 'POST'])(self.add_user_to_project)
        router('/remove_user_from_project', methods=['GET', 'POST'])(self.remove_user_from_project)
        router('/remove_assigned_user', methods=['GET', 'POST'])(self.remove_assigned_user)
        router('/create_project', methods=['GET', 'POST'])(self.create_project)
        router('/edit_project', methods=['GET', 'POST'])(self.edit_project)
        router('/delete_project', methods=['GET', 'POST'])(self.delete_project)
        router('/create_user', methods=['GET', 'POST'])(self.create_user)
        router('/delete_users', methods=['POST'])(self.delete_users)
        router('/admin')(self.admin)
        router('/passwordReset', methods=['GET', 'POST'])(self.passwordReset)
        router('/logout')(self.logout)
        router('/get_user_status', methods=['GET'])(self.get_user_status)
        router('/modify_user', methods=['GET', 'POST'])(self.modify_user)
        router('/setProjectId/<int:project_id>')(self.setProjectId)
        self.database = databaseManager()
        self.list_operation_manager = listOperationsManager()
        self.database.create_connection(os.path.join(os.getcwd(), 'Code/database.db'))
        self.database.create_tables()
        self.project_id = 1
        self.user_id = 0
        self.user_role = "user"
 
    def index(self):
        if not self.user_logged_in:
            return redirect(url_for('login'))
        elif self.user_role == "admin":
            return redirect(url_for('admin'))
        elif self.user_role == "supervisor":
            return redirect(url_for('supervisor'))
        projects = self.database.get_all_from_table("projects")
        tasks = self.database.get_all_from_table("tasks")
        users_in_projects = self.database.get_all_from_table("project_users")
        assigned_projects = []
        for project in projects:
            for project_user in users_in_projects:
                if project_user[1] == project[0] and project_user[3] == self.user_id:
                    project = [project[0], project[1], project[2], project[3], project[4], project[5]]
                    project.append([task[1] for task in tasks if task[6] == project[0]])
                    assigned_projects.append(project)
        return render_template('index.html', projects=assigned_projects)

    def setProjectId(self, project_id):
        self.project_id = project_id
        return redirect(url_for('tasks'))

    def login(self):
        form = LoginForm()
        username = form.username.data
        password = form.password.data
        if form.validate_on_submit():
            thisUser = self.database.find_user(username=username)
            if thisUser:
                # Check the password
                if check_password_hash(thisUser[2], password) or password == thisUser[2]:
                    self.user_logged_in = True
                    self.user_id = thisUser[0]
                    self.user_role = thisUser[3]
                    return redirect(url_for('index'))
                else:
                    print("Password incorrect, please try again.")
                    return render_template("login.html", form=form, message="Password incorrect, please try again.")
            else:
                print("User does not exist, please try again.")
                return render_template("login.html", form=form, message="User does not exist, please try again.")
        return render_template("login.html", form=form)

    def load_tasks(self):
        tasks = self.database.get_all_from_table("tasks")
        for task in tasks:
            if task[6] != self.project_id:
                tasks.remove(task)
        return tasks

    def passwordReset(self):
        form = PasswordResetForm()
        username = form.username.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        if form.validate_on_submit():
            thisUser = self.database.find_user(username=username)
            if thisUser:
                # Check the password
                if password == confirm_password:
                    hashed_password = generate_password_hash(password)
                    self.database.update_user(user_id=thisUser[0], password=hashed_password)
                    self.user_logged_in = True
                    self.user_id = thisUser[0]
                    self.user_role = thisUser[3]
                    flash("Password reset successfully", "success")
                    return redirect(url_for('index'))
                else:
                    return render_template("login.html", form=form, message="Passwords do not match, please try again.")
            else:
                return render_template("login.html", form=form, message="User does not exist, please try again.")
        return render_template("passwordReset.html", form=form)

    def supervisor(self):
        if self.user_role == "user":
            flash("You are not authorised to view this page\nMust be a supervisor or admin", "danger")
            return redirect(url_for('index'))
        projects = self.database.get_all_from_table("projects")
        project_users = self.database.get_all_from_table("project_users")
        users_in_projects = []
        tasks = self.load_tasks()
        theseProjects = []
        for project in projects:
            thisProject = []
            for atr in project:
                thisProject.append(atr)
            completed_tasks = 0
            total_tasks = 0
            project_tasks = []
            for task in tasks:
                if task[6] == project[0]:
                    total_tasks += 1
                    project_tasks.append(f"{task[1]} - {task[3]}")
                    if task[3] == "Completed":
                        completed_tasks += 1
            thisProject.append(project_tasks)
            thisProject.append(f"{completed_tasks} of {total_tasks} tasks completed")
            theseProjects.append(thisProject)
        current_project_id = 1
        current_user_names = []
        for row in project_users:
            if row[1] != current_project_id:
                users_in_projects.append(current_project_id)
                users_in_projects.append(current_user_names)
                current_user_names = []
                current_project_id = row[1]
            else:
                current_user_names.append(row[4])
        projects = theseProjects
        form = UsersInProjectsForm()
        form1 = RemoveProjectUsersForm()
        form2 = EditProjectForm()
        users = self.database.get_all_from_table("users")
        return render_template('supervisor.html', projects=projects, users=users, form=form, users_in_projects=users_in_projects, form1=form1, form2=form2)
    
    def admin(self):
        form = CreateProjectForm()
        form1 = CreateUserForm()
        form2 = UpdateUserDetailsForm()
        form3 = UsersInProjectsForm()
        users = self.database.get_all_from_table("users")
        if self.user_role != "admin":
            flash("You are not authorised to view this page\nMust be an admin", "danger")
            return redirect(url_for('index'))
        return render_template('admin.html', form=form, form1=form1, form2=form2, form3=form3, users=users)

    def tasks(self):
        tasks = self.load_tasks()
        form = UpdateProgressForm()
        form1 = EditTaskForm()
        form2 = RemoveAssignedUsersForm()
        project = self.database.find_project(project_id=self.project_id)
        project_tasks = []
        for task in tasks:
            if task[6] == self.project_id:
                project_tasks.append(task)
        tasks = project_tasks
        task_updates = self.database.get_all_from_table("task_updates")[::-1]
        assigned_tasks = self.database.get_all_from_table("assigned_tasks")
        users = self.database.get_all_from_table("users")
        return render_template('tasks.html', tasks=tasks, project=project, task_updates=task_updates, assigned_tasks=assigned_tasks, users=users, form=form, form1=form1, form2=form2)
    
    def search_tasks(self):
        tasks = self.load_tasks()
        form = UpdateProgressForm()
        form1 = EditTaskForm()
        search_term = request.get_json('search_term')
        task_titles = [task[1] for task in tasks]
        search_results = []
        thisResult = self.list_operation_manager.binary_search(task_titles, search_term)
        while thisResult != -1:
            search_results.append(tasks[thisResult])
            task_titles.remove(task_titles[thisResult])
            thisResult = self.list_operation_manager.binary_search(task_titles, search_term)
        project = self.database.find_project(project_id=self.project_id)
        task_updates = self.database.get_all_from_table("task_updates")[::-1]
        assigned_tasks = self.database.get_all_from_table("assigned_tasks")
        users = self.database.get_all_from_table("users")
        return render_template('tasks.html', tasks=search_results, project=project, task_updates=task_updates, assigned_tasks=assigned_tasks, users=users, form=form, form1=form1)

    def create_task(self):
        task_title = request.form['task-title']
        task_details = request.form['task-details']
        due_date = datetime.strptime(request.form['task-due-date'], "%Y-%m-%d")
        task_due_date = due_date.strftime("%d-%m-%Y")
        task_assigned_date = datetime.now().strftime("%d-%m-%Y")
        task_status = 'New'
        self.database.add_task(task_title, task_details, task_status, task_assigned_date, task_due_date, self.project_id)
        task_id = self.database.get_last_row_id("tasks")[0]
        self.database.add_assigned_task(task_id=task_id, task_title=task_title, assigned_user_id=self.user_id, assigned_username=self.database.find_user(user_id=self.user_id)[1], project_id=self.project_id)
        return redirect(url_for('tasks'))
    
    def sort_tasks(self):
        tasks = self.load_tasks()
        form = UpdateProgressForm()
        form1 = EditTaskForm()
        sort_type = request.get_json('sort_type')
        sorted_tasks = self.list_operation_manager.categorise_data(tasks, sort_type)
        project = self.database.find_project(project_id=self.project_id)
        task_updates = self.database.get_all_from_table("task_updates")[::-1]
        assigned_tasks = self.database.get_all_from_table("assigned_tasks")
        users = self.database.get_all_from_table("users")
        return render_template('tasks.html', tasks=sorted_tasks, project=project, task_updates=task_updates, assigned_tasks=assigned_tasks, users=users, form=form, form1=form1)

    def filter_tasks(self):
        tasks = self.load_tasks()
        form = UpdateProgressForm()
        form1 = EditTaskForm()
        filter_word = request.get_json('filter_word')
        filtered_tasks = self.list_operation_manager.filter_data(tasks, "status", filter_word)
        project = self.database.find_project(project_id=self.project_id)
        task_updates = self.database.get_all_from_table("task_updates")[::-1]
        assigned_tasks = self.database.get_all_from_table("assigned_tasks")
        users = self.database.get_all_from_table("users")
        return render_template('tasks.html', tasks=filtered_tasks, project=project, task_updates=task_updates, assigned_tasks=assigned_tasks, users=users, form=form, form1=form1)
    
    def update_progress(self):
        form = UpdateProgressForm()
        if form.validate_on_submit():
            update = form.progress_update.data
            if not update:
                flash("No progress update provided", "danger")
                return redirect(url_for('tasks'))
            row_id = self.database.add_task_update(project_id=self.project_id, progress_update=update)
            if row_id:
                flash("Progress update added successfully", "success")
            else:
                flash("Failed to add progress update", "danger")
        return redirect(url_for('tasks'))

    def search_projects(self, search_term):
        projects = self.database.get_all_from_table("projects")
        project_titles = [project[1] for project in projects]
        search_results = []
        thisResult = self.list_operation_manager.binary_search(project_titles, search_term)
        while thisResult != -1:
            search_results.append(projects[thisResult])
            project_titles.remove(project_titles[thisResult])
            thisResult = self.list_operation_manager.binary_search(project_titles, search_term)
        form = UsersInProjectsForm()
        users = self.database.get_all_from_table("users")
        return render_template('supervisor.html', projects=search_results, users=users, form=form)    
    
    def filter_projects(self, filter_type, filter_word):
        projects = self.database.get_all_from_table("projects")
        filtered_projects = self.list_operation_manager.filter_data(projects, filter_type, filter_word)
        form = UsersInProjectsForm()
        users = self.database.get_all_from_table("users")
        return render_template('supervisor.html', projects=filtered_projects, users=users, form=form)
        
    def sort_projects(self, sort_type):
        projects = self.database.get_all_from_table("projects")
        sorted_projects = self.list_operation_manager.categorise_data(projects, sort_type)
        form = UsersInProjectsForm()
        users = self.database.get_all_from_table("users")
        return render_template('supervisor.html', projects=sorted_projects, users=users, form=form)

    def add_user_to_project(self):
        form = UsersInProjectsForm()
        project_title = form.project_title.data
        usernames = request.form.get('username').split(",")  # Split the comma-separated string into a list
        if not usernames:
            flash("No users selected", "danger")
            return redirect(url_for('admin'))
        print(usernames)
        project_id = self.database.find_project(project_title=project_title)[0]
        for username in usernames:
            user_id = self.database.find_user(username=username.strip())[0]
            print(user_id)
            rowId = self.database.add_user_into_project(project_id=project_id, user_id=user_id, project_title=project_title, username=username.strip())
        if rowId:
            flash("User(s) added to selected project successfully", "success")
        else:
            flash("User(s) not added to selected project", "danger")
        return redirect(url_for('index'))
    
    def remove_user_from_project(self):
        form = RemoveProjectUsersForm()
        users = form.selected_users.data
        project_title = form.project_title.data
        for user in users:
            user_id = self.database.find_user(username=user)[0]
            project_id = self.database.find_project(project_title=project_title)[0]
            id = self.database.find_user_in_project(user_id=user_id, project_id=project_id)[0]
            self.database.remove_user_from_project(id=id)
        return redirect(url_for('supervisor'))
    
    def remove_assigned_user(self):
        form = RemoveAssignedUsersForm()
        users = request.form.get('selected_users').split(",") # Split the comma-separated string into a list 
        task_id = request.form.get('task_id')
        for user in users:
            id = self.database.find_assigned_task(assigned_user_id=int(user), task_id=task_id, project_id=self.project_id)[0]
            row_id = self.database.remove_assigned_task(assigned_task_id=id)
            if row_id:
                flash("Assigned user removed successfully", "success")
            else:
                flash("Assigned user not removed", "danger")
        return redirect(url_for('tasks'))

    def create_project(self):
        form = CreateProjectForm()
        if form.validate_on_submit():
            project_title = form.project_title.data
            project_details = form.project_details.data
            project_status = form.project_status.data
            project_review = form.project_review.data
            project_owner = form.project_owner.data
            rowId = self.database.add_project(project_title, project_details, project_status, project_review, project_owner)
            if rowId:
                flash("Project added successfully", "success")
            return redirect(url_for('index'))
        else:
            flash("Project not added", "danger")
        return redirect(url_for('admin'))
    
    def create_user(self):
        form = CreateUserForm()
        username = form.username.data
        password = form.password.data
        role = form.role.data.lower()
        team = form.team.data.lower()
        hashed_password = generate_password_hash(password)
        if form.validate_on_submit():
            rowID = self.database.add_user(username, hashed_password, role, team)
            if rowID:
                flash("User added successfully", "success")
            return redirect(url_for('index'))
        return redirect(url_for('admin'))
    
    def delete_users(self):
        # Retrieve the selected user IDs from the form
        selected_users = request.form.get('selected_users')  # This will be a comma-separated string
        if selected_users:
            user_ids = selected_users.split(',')  # Convert the string into a list of user IDs
            # Process the user IDs (e.g., delete them from the database)
            for user_id in user_ids:
                self.database.delete_user(user_id=user_id)
            flash("Selected users have been deleted successfully.", "success")
        else:
            flash("No users were selected for deletion.", "danger")
        return redirect(url_for('admin'))

    def edit_project(self):
        project_id = request.form.get('project_id') # Get the project ID from the form
        form = EditProjectForm()
        project_title = ""
        project_details = ""
        project_status = ""
        project_review = ""
        project_owner = ""
        if form.validate_on_submit():
            if form.project_title.data:
                project_title = form.project_title.data
            if form.project_details.data:
                project_details = form.project_details.data
            if form.project_status.data:
                project_status = form.project_status.data
            if form.project_review.data:
                project_review = form.project_review.data
            if form.project_owner.data:
                project_owner = form.project_owner.data
            row_id = self.database.update_project(project_id=project_id, project_title=project_title, project_details=project_details, project_status=project_status, project_review=project_review, project_owner=project_owner)
            if row_id:
                flash("Project updated successfully", "success")
            else:
                flash("Project not updated", "danger")
        return redirect(url_for('supervisor'))

    def delete_project(self, project_id):
        deleted_project = self.database.find_task(project_id=project_id)
        self.database.delete_project(project_id=project_id)
        self.deleted_projects.append(deleted_project)
        projects = self.database.get_all_from_table("projects")
        return render_template('projects.html', projects=projects)

    def modify_user(self):
        form = UpdateUserDetailsForm()
        username = form.username.data
        user = self.database.find_user(username=username)
        user_id = user[0]
        password = form.password.data
        if password:
            hashed_password = generate_password_hash(password)
        else:
            hashed_password = ""
        role = form.role.data.lower()
        if role == user[3]:
            role = ""
        team = form.team.data.lower()
        if team == user[4]:
            team = ""
        if form.validate_on_submit():
            self.database.update_user(user_id=user_id, password=hashed_password, role=role, team=team)
            flash("User updated successfully", "success")
            return redirect(url_for('index'))
        return redirect(url_for('admin'))

    def edit_task(self):
        task_id = request.form.get('task_id') # Get the task ID from the form     
        form = EditTaskForm()   
        task_title = ""
        task_details = ""
        assigned_date = ""
        due_date = ""
        task_status = ""
        if form.validate_on_submit():
            if form.task_title.data:
                task_title = form.task_title.data
            if form.task_details.data:
                task_details = form.task_details.data
            if form.task_assigned_date.data:
                assigned_date = form.task_assigned_date.data
            if form.task_due_date.data:
                due_date = form.task_due_date.data
            if form.task_status.data:
                task_status = form.task_status.data
            row_id = self.database.update_task(task_id=task_id, task_title=task_title, task_details=task_details, task_status=task_status, task_assigned_date=assigned_date, task_due_date=due_date, project_id=self.project_id)
            if row_id:
                flash("Task updated successfully", "success")
            else:
                flash("Task not updated", "danger")
        return redirect(url_for('tasks'))
    
    def delete_task(self, task_id):
        deleted_task = self.database.find_task(task_id=task_id)
        self.database.delete_task(task_id=task_id)
        self.deleted_tasks.append(deleted_task)
        return redirect(url_for('tasks')) 
    
    def show_deleted_tasks(self):
        return render_template('tasks.html', deleted_tasks=self.deleted_tasks)
    
    def assign_users(self):
        selected_users = request.form.get('selected_users')  # Get the selected user IDs from the form
        task_id = request.form.get('task_id')  # Get the task ID
        if selected_users and task_id:
            user_ids = selected_users.split(",")  # Convert the string into a list of user IDs
            for user_id in user_ids:
                self.database.add_assigned_task(
                    task_id=task_id,
                    task_title=self.database.find_task(task_id=task_id)[1],
                    assigned_user_id=user_id,
                    assigned_username=self.database.find_user(user_id=user_id)[1],
                    project_id=self.project_id
                )
            flash("Users assigned successfully", "success")
        else:
            print("Selected users:", selected_users)
            print("Task id:", task_id)
            flash("Failed to assign users", "danger")
        return redirect(url_for('tasks'))

    def get_user_status(self):
        return [self.user_logged_in, self.user_id, self.user_role]
    
    def logout(self):
        self.user_logged_in = False
        self.user_id = 0
        self.user_role = "user"
        return redirect(url_for('index'))
        
app = Flask(__name__)
app.config['SECRET_KEY'] = 'randomString'
myObj = myClass( app.route )
app.register_blueprint(myObj.blueprint)
app.run(host='localhost', port=5000)