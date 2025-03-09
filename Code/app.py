from flask import Flask, request, jsonify, render_template, Blueprint, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

from use_database import databaseManager
from search_sort import listOperationsManager
from forms import LoginForm, CreateUserForm, UpdateUserDetailsForm, CreateProjectForm, UpdateProgressForm, EditTaskForm, UsersInProjectsForm
 
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
        router('/add_user_to_project', methods=['GET', 'POST'])(self.add_user_to_project)
        router('/remove_user_from_project')(self.remove_user_from_project)
        router('/create_project', methods=['GET', 'POST'])(self.create_project)
        router('/edit_project')(self.edit_project)
        router('/delete_project')(self.delete_project)
        router('/create_user', methods=['GET', 'POST'])(self.create_user)
        router('/admin')(self.admin)
        router('/passwordReset')(self.passwordReset)
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
        project_tasks = []
        assigned_projects = []
        for project in projects:
            for project_user in users_in_projects:
                if project_user[1] == project[0] and project_user[3] == self.user_id:
                    assigned_projects.append(project)
                    project_tasks.append({project[1]: [task[1] for task in tasks if task[6] == project[0]]})
        return render_template('index.html', projects=assigned_projects, project_tasks=project_tasks)

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
        return tasks

    def passwordReset(self):
        pass

    def supervisor(self):
        if self.user_role != "supervisor":
            flash("You are not authorised to view this page\nMust be a supervisor", "danger")
            return redirect(url_for('index'))
        projects = self.database.get_all_from_table("projects")
        return render_template('SupervisorHomePage.html', projects=projects)
    
    def admin(self):
        form = CreateProjectForm()
        form1 = CreateUserForm()
        form2 = UpdateUserDetailsForm()
        form3 = UsersInProjectsForm()
        if self.user_role != "admin":
            flash("You are not authorised to view this page\nMust be an admin", "danger")
            return redirect(url_for('index'))
        return render_template('admin.html', form=form, form1=form1, form2=form2, form3=form3)

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
        due_date = datetime.strptime(request.form['task-due-date'], "%Y-%m-%d")
        task_due_date = due_date.strftime("%d-%m-%Y")
        task_assigned_date = datetime.now().strftime("%d-%m-%Y")
        task_status = 'New'
        self.database.add_task(task_title, task_details, task_status, task_assigned_date, task_due_date, self.project_id)
        task_id = self.database.get_last_row_id("tasks")
        self.database.add_assigned_task(task_id=task_id, task_title=task_title, assigned_user_id=self.user_id, assigned_username=self.database.find_user(user_id=self.user_id)[1], project_id=self.project_id)
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

    def add_user_to_project(self):
        form = UsersInProjectsForm()
        if form.validate_on_submit():
            project_title = form.project_title.data
            usernames = form.username.data
            project_id = self.database.find_project(project_title=project_title)[0]
            for username in usernames:
                user_id = self.database.find_user(username=username)[0]
                rowId = self.database.add_user_into_project(project_id=project_id, user_id=user_id, project_title=project_title, username=username)
            if rowId:
                flash("User(s) added to selected project successfully", "success")
            return redirect(url_for('index'))
        else:
            flash("User(s) not added to selected project", "danger")
        return redirect(url_for('admin'))

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

    def edit_project(self, project_id):
        self.database.update_project(project_id=project_id)
        return redirect(url_for('index'))

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

    def edit_task(self, task_id):
        self.database.update_task(task_id=task_id)
        return redirect(url_for('tasks'))
    
    def delete_task(self, task_id):
        deleted_task = self.database.find_task(task_id=task_id)
        self.database.delete_task(task_id=task_id)
        self.deleted_tasks.append(deleted_task)
        return redirect(url_for('tasks')) 
    
    def show_deleted_tasks(self):
        return render_template('tasks.html', deleted_tasks=self.deleted_tasks)
    
    def assign_users(self, user_ids, task_id):
        thisTask = self.database.find_task(task_id=task_id)
        for user_id in user_ids:
            thisUser = self.database.find_user(user_id=user_id)
            self.database.add_assigned_task(task_id=task_id, task_title=thisTask[1], assigned_user_id=user_id, assigned_username=thisUser[1], project_id=thisTask[6])
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