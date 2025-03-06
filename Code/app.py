from flask import Flask, request, jsonify, render_template, Blueprint, redirect, url_for, flash
from use_database import databaseManager
from datetime import datetime
from search_sort import listOperationsManager
from forms import LoginForm
import os
 
class myClass():
    def __init__(self, router):
        self.blueprint = Blueprint('myClass', __name__)
        self.user_logged_in = False
        self.deleted_tasks = []
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
        self.database = databaseManager()
        self.list_operation_manager = listOperationsManager()
        self.database.create_connection(os.path.join(os.getcwd(), 'Code/database.db'))
        self.database.create_tables()
        self.project_id = 1
 
    def index(self):
        return render_template('index.html')

    def login(self):
        form = LoginForm()
        username = form.username.data
        password = form.password.data
        if form.validate_on_submit():
            thisUser = self.database.find_user(username=username)
            if thisUser:
                # Check the password
                if thisUser.password == password:
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

    def tasks(self):
        tasks = self.load_tasks()
        return render_template('tasks.html', tasks=tasks)
    
    def search_tasks(self, search_term):
        tasks = self.load_tasks()
        task_titles = [task["title"] for task in tasks]
        search_results = self.binary_search(task_titles, search_term)
        return render_template('tasks.html', tasks=search_results)

    def create_task(self):
        task_title = request.form['todo-input']
        self.database.add_task(task_title, task_title, "New", datetime.now().strftime("%d-%m-%Y %H:%M"), datetime.now().strftime("%d-%m-%Y %H:%M"), self.project_id)
        tasks = self.load_tasks()
        return render_template('tasks.html', tasks=tasks)
    
    def sort_tasks(self, sort_type):
        tasks = self.load_tasks()
        sorted_tasks = self.list_operation_manager.categorise_data(tasks, sort_type)
        return render_template('tasks.html', tasks=sorted_tasks)

    def filter_tasks(self, filter_type):
        tasks = self.load_tasks()
        filtered_tasks = self.list_operation_manager.filter_data(tasks, filter_type)
        return render_template('tasks.html', tasks=filtered_tasks)
    
    def update_progress(self, project_id, update):
        self.database.add_task_update(project_id=project_id, progress_update=update)
        task_updates = [{"project_id": project_id, "progress_update": update, "date": datetime.now().strftime("%d-%m-%Y %H:%M")}]
        return render_template('tasks.html', taskUpdates=task_updates)
    
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
            self.database.add_assigned_task(task_id=task_id, task_title=thisTask["title"], assigned_user_id=user_id, assigned_username=thisUser["username"], project_id=thisTask["project_id"])
        tasks = self.load_tasks()
        assigned_tasks = self.database.get_all_from_table("assigned_tasks")
        assigned_users = []
        for task in assigned_tasks:
            assigned_users.append({task["task_id"]: task["assigned_username"]})
        return render_template('tasks.html', tasks, assigned_users)
        
app = Flask(__name__)
myObj = myClass( app.route )
app.register_blueprint(myObj.blueprint)
app.config['SECRET_KEY'] = 'randomString'
app.run(host='localhost', port=5000)
