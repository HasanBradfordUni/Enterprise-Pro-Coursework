from flask import Flask, request, jsonify, render_template, Blueprint, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import CSRFProtect
from datetime import datetime, timedelta
import os

from use_database import databaseManager
from search_sort import listOperationsManager
from forms import LoginForm, CreateUserForm, UpdateUserDetailsForm, CreateProjectForm, UpdateProgressForm, EditTaskForm
 
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
        router('/sort_tasks')(self.sort_tasks)
        router('/filter_tasks')(self.filter_tasks)
        router('/update_progress')(self.update_progress)
        router('/edit_task')(self.edit_task)
        router('/delete_task')(self.delete_task)
        router('/show_deleted_tasks')(self.show_deleted_tasks)
        router('/assign_users')(self.assign_users)
        router('/search_tasks')(self.search_tasks)
        router('/login', methods=['GET', 'POST'])(self.login)
        router('/search_projects')(self.search_projects)
        router('/filter_projects')(self.filter_projects)
        router('/sort_projects')(self.sort_projects)
        router('/add_user_to_project')(self.add_user_to_project)
        router('/remove_user_from_project')(self.remove_user_from_project)
        router('/create_project', methods=['GET', 'POST'])(self.create_project)
        router('/edit_project')(self.edit_project)
        router('/delete_project')(self.delete_project)
        router('/create_user', methods=['GET', 'POST'])(self.create_user)
        router('/admin')(self.admin)
        self.database = databaseManager()
        self.list_operation_manager = listOperationsManager()
        self.database.create_connection(os.path.join(os.getcwd(), 'Code/database.db'))
        self.database.create_tables()
        self.project_id = 1
        self.user_id = 0
        self.user_role = "user"
 
    def index(self):
        projects = self.database.get_all_from_table("projects")
        tasks = self.database.get_all_from_table("tasks")
        project_tasks = []
        for project in projects:
            project_tasks.append({project[1]: [task[1] for task in tasks if task[6] == project[0]]})
        return render_template('index.html', projects=projects, project_tasks=project_tasks)

    def login(self):
        form = LoginForm()
        username = form.username.data
        password = form.password.data
        if form.validate_on_submit():
            thisUser = self.database.find_user(username=username)
            print(thisUser)
            if thisUser:
                # Check the password
                if check_password_hash(thisUser[2], password) or password == thisUser[2]:
                    print("Login successful")
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
        return tasks

    def supervisor(self):
        return render_template('SupervisorHomePage.html')
    
    def admin(self):
        form = CreateProjectForm()
        form1 = CreateUserForm()
        return render_template('admin.html', form=form, form1=form1)

    def tasks(self):
        tasks = self.load_tasks()
        project = self.database.find_project(project_id=self.project_id)
        task_updates = self.database.get_all_from_table("task_updates")
        assigned_tasks = self.database.get_all_from_table("assigned_tasks")
        return render_template('tasks.html', tasks=tasks, project=project, task_updates=task_updates, assigned_tasks=assigned_tasks)
    
    def search_tasks(self, search_term):
        tasks = self.load_tasks()
        task_titles = [task["title"] for task in tasks]
        search_results = self.binary_search(task_titles, search_term)
        project = self.database.find_project(project_id=self.project_id)
        task_updates = self.database.get_all_from_table("task_updates")
        assigned_tasks = self.database.get_all_from_table("assigned_tasks")
        return render_template('tasks.html', tasks=search_results, project=project, task_updates=task_updates, assigned_tasks=assigned_tasks)

    def create_task(self):
        task_title = request.form['task-title']
        task_details = request.form['task-details']
        print(request.form['task-due-date'])
        due_date = datetime.now() + timedelta(days=10)
        task_due_date = due_date.strftime("%d-%m-%Y")
        task_assigned_date = datetime.now().strftime("%d-%m-%Y")
        task_status = 'New'
        self.database.add_task(task_title, task_details, task_due_date, task_assigned_date, task_status, self.project_id)
        return redirect(url_for('tasks'))
    
    def sort_tasks(self, sort_type):
        tasks = self.load_tasks()
        sorted_tasks = self.list_operation_manager.categorise_data(tasks, sort_type)
        project = self.database.find_project(project_id=self.project_id)
        task_updates = self.database.get_all_from_table("task_updates")
        assigned_tasks = self.database.get_all_from_table("assigned_tasks")
        return render_template('tasks.html', tasks=sorted_tasks, project=project, task_updates=task_updates, assigned_tasks=assigned_tasks)

    def filter_tasks(self, filter_type):
        tasks = self.load_tasks()
        filtered_tasks = self.list_operation_manager.filter_data(tasks, filter_type)
        project = self.database.find_project(project_id=self.project_id)
        task_updates = self.database.get_all_from_table("task_updates")
        assigned_tasks = self.database.get_all_from_table("assigned_tasks")
        return render_template('tasks.html', tasks=filtered_tasks, project=project, task_updates=task_updates, assigned_tasks=assigned_tasks)
    
    def update_progress(self, project_id, update):
        self.database.add_task_update(project_id=project_id, progress_update=update)
        task_updates = [{"project_id": project_id, "progress_update": update, "date": datetime.now().strftime("%d-%m-%Y %H:%M")}]
        project = self.database.find_project(project_id=project_id)
        tasks = self.load_tasks()
        return render_template('tasks.html', tasks=tasks, project=project, task_updates=task_updates)

    def search_projects(self, search_term):
        projects = self.database.get_all_from_table("projects")
        project_titles = [project["title"] for project in projects]
        search_results = self.list_operation_manager.binary_search(project_titles, search_term)
        return render_template('projects.html', projects=search_results)
    
    def filter_projects(self, filter_type):
        projects = self.database.get_all_from_table("projects")
        filtered_projects = self.list_operation_manager.filter_data(projects, filter_type)
        return render_template('projects.html', projects=filtered_projects)
    
    def sort_projects(self, sort_type):
        projects = self.database.get_all_from_table("projects")
        sorted_projects = self.list_operation_manager.categorise_data(projects, sort_type)
        return render_template('projects.html', projects=sorted_projects)

    def add_user_to_project(self, user_id, project_id):
        project_title = self.database.find_project(project_id=project_id)[1]
        username = self.database.find_user(user_id=user_id)[1]
        self.database.add_user_into_project(project_id=project_id, user_id=user_id, project_title=project_title, username=username)
        return redirect(url_for('index'))

    def remove_user_from_project(self, user_id, project_id):
        id = self.database.find_user_in_project(user_id=user_id, project_id=project_id)[0]
        self.database.remove_user_from_project(id=id)
        return redirect(url_for('index'))

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
                print("Project added successfully")
            return redirect(url_for('index'))
        else:
            print("Project not added")
            print(form.errors)
        return redirect(url_for('admin'))
    
    def create_user(self):
        form = CreateUserForm()
        username = form.username.data
        password = form.password.data
        role = form.role.data.lower()
        team = form.team.data.lower()
        hashed_password = generate_password_hash(password)
        if form.validate_on_submit():
            self.database.add_user(username, hashed_password, role, team)
            print("User added successfully")
            return redirect(url_for('index'))
        else:
            print("User not added")
            print(form.errors)
        return redirect(url_for('admin'))

    def edit_project(self, project_id):
        self.database.update_project(project_id=project_id)
        return redirect(url_for('index'))

    def delete_project(self, project_id):
        deleted_project = self.database.find_task(project_id=project_id)
        self.database.delete_project(project_id=project_id)
        self.deleted_projects.append(deleted_project)
        projects = self.database.get_all_from_table("projects")
        return render_template('projects.html', projects=projects)

    def edit_task(self, task_id):
        self.database.edit_task(task_id=task_id)
        tasks = self.load_tasks()
        return render_template('tasks.html', tasks=tasks)
    
    def delete_task(self, task_id):
        deleted_task = self.database.find_task(task_id=task_id)
        self.database.remove_task(task_id=task_id)
        self.deleted_tasks.append(deleted_task)
        tasks = self.load_tasks()
        return render_template('tasks.html', tasks=tasks)   
    
    def show_deleted_tasks(self):
        return render_template('tasks.html', deleted_tasks=self.deleted_tasks)
    
    def assign_users(self, user_ids, task_id):
        thisTask = self.database.find_task(task_id=task_id)
        for user_id in user_ids:
            thisUser = self.database.find_user(user_id=user_id)
            self.database.add_assigned_task(task_id=task_id, task_title=thisTask[1], assigned_user_id=user_id, assigned_username=thisUser[1], project_id=thisTask[6])
        tasks = self.load_tasks()
        assigned_tasks = self.database.get_all_from_table("assigned_tasks")
        assigned_users = []
        for task in assigned_tasks:
            assigned_users.append({task[1]: task[4]})
        return render_template('tasks.html', tasks, assigned_users)
        
app = Flask(__name__)
app.config['SECRET_KEY'] = 'randomString'
myObj = myClass( app.route )
app.register_blueprint(myObj.blueprint)
app.run(host='localhost', port=5000)