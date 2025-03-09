import sqlite3
from sqlite3 import Error
from datetime import datetime

class databaseManager:
    def __init__(self):
        self.connection = None

    def create_connection(self, path):
        try:
            connection = sqlite3.connect(path, check_same_thread=False)
            self.connection = connection
            #print(self.connection)
            return "connection to SQLite DB successful"
        except Error as e:
            #print(self.connection)
            return f"The error '{e}' occurred"
    
    def get_last_row_id(self, table_name):
        cursor = self.connection.cursor()
        id_type = f"{table_name[:-1]}_id"
        select_statement = f"""
    SELECT {id_type} FROM {table_name}
    ORDER BY {id_type} DESC
    LIMIT 1;
    """
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(select_statement)
            result = cursor.fetchone()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    def create_tables(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'User',
            team TEXT NOT NULL DEFAULT 'Police'
        );
        """

        self.execute_query(query)

        query = """
        CREATE TABLE IF NOT EXISTS projects (
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_title TEXT NOT NULL,
            project_details TEXT NOT NULL,
            project_status TEXT NOT NULL DEFAULT 'In Progress',
            project_review TEXT,
            project_owner TEXT NOT NULL,
            FOREIGN KEY (project_owner) REFERENCES users (username)
        );
        """

        self.execute_query(query)

        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_title TEXT NOT NULL,
            task_details TEXT NOT NULL,
            task_status TEXT NOT NULL DEFAULT 'New',
            task_assigned_date DATE NOT NULL,
            task_due_date DATE NOT NULL,
            project_id INTEGER NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (project_id)
        );
        """

        self.execute_query(query)

        query = """
        CREATE TABLE IF NOT EXISTS task_updates (
            task_update_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            progress_update TEXT,
            new_status TEXT,
            update_date DATE NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (project_id)
        );
        """

        self.execute_query(query)

        query = """
        CREATE TABLE IF NOT EXISTS project_users (
            project_user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            project_title TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (project_id),
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        );
        """

        self.execute_query(query)

        query = """
        CREATE TABLE IF NOT EXISTS assigned_tasks (
            assigned_task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER NOT NULL,
            task_title TEXT NOT NULL,
            assigned_user_id INTEGER NOT NULL,
            assigned_username TEXT NOT NULL,
            project_id INTEGER NOT NULL,
            FOREIGN KEY (task_id) REFERENCES tasks (task_id),
            FOREIGN KEY (assigned_user_id) REFERENCES users (user_id),
            FOREIGN KEY (project_id) REFERENCES projects (project_id),
            FOREIGN KEY (assigned_username) REFERENCES users (username)
        );
        """

        self.execute_query(query)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            return "Query executed successfully"
        except Error as e:
            return f"The error '{e}' occurred"
        
    def add_user(self, username, password, role, team):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        INSERT INTO users (username, password, role, team)
        VALUES ('{username}', '{password}', '{role}', '{team}')
        """)
        self.connection.commit()
        return cursor.lastrowid

    def add_project(self, project_title, project_details, project_status, project_review, project_owner):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        INSERT INTO projects (project_title, project_details, project_status, project_review, project_owner)
        VALUES ('{project_title}', '{project_details}', '{project_status}', '{project_review}', '{project_owner}')
        """)
        self.connection.commit()
        return cursor.lastrowid

    def add_task(self, task_title, task_details, task_status, task_assigned_date, task_due_date, project_id):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        INSERT INTO tasks (task_title, task_details, task_status, task_assigned_date, task_due_date, project_id)
        VALUES ('{task_title}', '{task_details}', '{task_status}', '{task_assigned_date}', '{task_due_date}', '{project_id}')
        """)
        self.connection.commit()
        return cursor.lastrowid

    def add_task_update(self, project_id, progress_update="", new_status="", update_date=datetime.now().strftime("%d-%m-%Y %H:%M")):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        INSERT INTO task_updates (project_id, progress_update, new_status, update_date)
        VALUES ('{project_id}', '{progress_update}', '{new_status}', '{update_date}')
        """)
        self.connection.commit()
        return cursor.lastrowid

    def add_user_into_project(self, project_id, project_title, user_id, username):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        INSERT INTO project_users (project_id, project_title, user_id, username)
        VALUES ('{project_id}', '{project_title}', '{user_id}', '{username}')
        """)
        self.connection.commit()
        return cursor.lastrowid

    def add_assigned_task(self, task_id, task_title, assigned_user_id, assigned_username, project_id):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        INSERT INTO assigned_tasks (task_id, task_title, assigned_user_id, assigned_username, project_id)
        VALUES ('{task_id}', '{task_title}', '{assigned_user_id}', '{assigned_username}', '{project_id}') 
        """)
        self.connection.commit()
        return cursor.lastrowid

    def find_user(self, user_id=0, username="", role="", team=""):
        cursor = self.connection.cursor()
        if user_id != 0:
            cursor.execute(f"""
            SELECT * FROM users WHERE user_id = {user_id}
            """)
        elif role == "" or team == "":
            cursor.execute(f"""
            SELECT * FROM users WHERE username = '{username}'
            """)
        else:
            cursor.execute(f"""
        SELECT * FROM users WHERE role = '{role}' AND team = '{team}' AND username = '{username}'
        """)
        return cursor.fetchone()
    
    def find_project(self, project_id=0, project_title="", project_details="", project_status="", project_review="", team="", project_owner=""):
        cursor = self.connection.cursor()
        if project_id != 0:
            cursor.execute(f"""
            SELECT * FROM projects WHERE project_id = {project_id}
            """)
        else:
            query = "SELECT * FROM projects WHERE 1=1"
            filters = {
                "project_title": project_title,
                "project_details": project_details,
                "project_status": project_status,
                "project_review": project_review,
                "team": team,
                "project_owner": project_owner
            }
            for key, value in filters.items():
                if value:
                    query += f" AND {key} = '{value}'"
            cursor.execute(query)
        return cursor.fetchone()
    
    def find_task(self, task_id=0, task_title="", project_id=0):
        cursor = self.connection.cursor()
        if task_id != 0:
            cursor.execute(f"""
            SELECT * FROM tasks WHERE task_id = {task_id}
            """)
        else:
            cursor.execute(f"""
            SELECT * FROM tasks WHERE task_title = '{task_title}' AND project_id = {project_id}
            """)
        return cursor.fetchone()

    
    def find_task_update(self, task_update_id=0, project_id=0, progress_update="", new_status="", update_date=False):
        cursor = self.connection.cursor()
        if task_update_id != 0:
            cursor.execute(f"""
            SELECT * FROM task_updates WHERE task_update_id = {task_update_id}
            """)
        else:
            query = "SELECT * FROM task_updates WHERE 1=1"
            filters = {
                "project_id": project_id,
                "progress_update": progress_update,
                "new_status": new_status,
                "update_date": update_date
            }
            for key, value in filters.items():
                if value:
                    if key == "update_date":
                        query += f" AND {key} = DATE('{value}')"
                    else:
                        query += f" AND {key} = '{value}'"
            cursor.execute(query)
        return cursor.fetchone()

    def find_user_in_project(self, project_user_id=0, project_id=0, user_id=0, username=""):
        cursor = self.connection.cursor()
        if project_user_id != 0:
            cursor.execute(f"""
            SELECT * FROM project_users WHERE project_user_id = {project_user_id}
            """)
        else:
            query = "SELECT * FROM project_users WHERE 1=1"
            filters = {
                "project_id": project_id,
                "user_id": user_id,
                "username": username
            }
            for key, value in filters.items():
                if value:
                    query += f" AND {key} = '{value}'"
            cursor.execute(query)
        return cursor.fetchone()
    
    def find_task_update(self, task_update_id=0, project_id=0, progress_update="", new_status="", update_date=False):
        cursor = self.connection.cursor()
        if task_update_id != 0:
            cursor.execute(f"""
            SELECT * FROM task_updates WHERE task_update_id = {task_update_id}
            """)
        else:
            query = "SELECT * FROM task_updates WHERE 1=1"
            filters = {
                "project_id": project_id,
                "progress_update": progress_update,
                "new_status": new_status,
                "update_date": update_date
            }
            for key, value in filters.items():
                if value:
                    if key == "update_date":
                        query += f" AND {key} = DATE('{value}')"
                    else:
                        query += f" AND {key} = '{value}'"
            cursor.execute(query)
        return cursor.fetchone()

    def find_user_in_project(self, project_user_id=0, project_id=0, user_id=0, username=""):
        cursor = self.connection.cursor()
        if project_user_id != 0:
            cursor.execute(f"""
            SELECT * FROM project_users WHERE project_user_id = {project_user_id}
            """)
        else:
            query = "SELECT * FROM project_users WHERE 1=1"
            filters = {
                "project_id": project_id,
                "user_id": user_id,
                "username": username
            }
            for key, value in filters.items():
                if value:
                    query += f" AND {key} = '{value}'"
            cursor.execute(query)
        return cursor.fetchone()

    def find_assigned_task(self, assigned_task_id=0, task_id=0, assigned_user_id=0, project_id=0):
        cursor = self.connection.cursor()
        if assigned_task_id != 0:
            cursor.execute(f"""
            SELECT * FROM assigned_tasks WHERE assigned_task_id = {assigned_task_id}
            """)
        else:
            cursor.execute(f"""
            SELECT * FROM assigned_tasks WHERE task_id = {task_id} AND assigned_user_id = {assigned_user_id} AND project_id = {project_id}
            """)
        return cursor.fetchone()

    def get_all_from_table(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        SELECT * FROM {table_name}
        """)
        return cursor.fetchall()
        
    def update_user(self, user_id=0, username="", password="", role="", team=""):
        cursor = self.connection.cursor()
        updates = { "username": username, "password": password, "role": role, "team": team }
        query = "UPDATE users SET " + ", ".join([f"{key} = '{value}'" for key, value in updates.items() if value != ""])
        
        if user_id != 0:
            query += f" WHERE user_id = {user_id}"
        else:
            query += f" WHERE username = '{username}'"
        
        cursor.execute(query)
        self.connection.commit()
        return cursor.lastrowid

    def update_project(self, project_id=0, project_title="", project_details="", project_status="", project_review="", project_owner=""):
        cursor = self.connection.cursor()
        updates = { "project_title": project_title, "project_details": project_details, "project_status": project_status, "project_review": project_review, "project_owner": project_owner }
        query = "UPDATE projects SET " + ", ".join([f"{key} = '{value}'" for key, value in updates.items() if value != ""])
        query += f" WHERE project_id = {project_id}"
        cursor.execute(query)
        self.connection.commit()
        return cursor.lastrowid

    def update_task(self, task_id=0, task_title="", task_details="", task_status="", task_assigned_date="", task_due_date="", project_id=0):
        cursor = self.connection.cursor()
        updates = { "task_title": task_title, "task_details": task_details, "task_status": task_status, "task_assigned_date": task_assigned_date, "task_due_date": task_due_date, "project_id": project_id }
        query = "UPDATE tasks SET " + ", ".join([f"{key} = {value}" if str(value).isdigit() and value != 0 else f"{key} = '{value}'" for key, value in updates.items() if value != ""])
        query += f" WHERE task_id = {task_id}"
        cursor.execute(query)
        self.connection.commit()
        return cursor.lastrowid

    def update_user_in_project(self, project_user_id=0, project_id=0, project_title="", user_id=0, username=""):
        cursor = self.connection.cursor()
        updates = { "project_title": project_title, "user_id": user_id, "username": username }
        query = "UPDATE project_users SET " + ", ".join([f"{key} = {value}" if str(value).isdigit() and value != 0 else f"{key} = '{value}'" for key, value in updates.items() if value != ""])
        
        if project_user_id != 0:
            query += f" WHERE project_user_id = {project_user_id}"
        else:
            query += f" WHERE project_id = {project_id} AND user_id = {user_id}"
        
        cursor.execute(query)
        self.connection.commit()
        return cursor.lastrowid

    def update_assigned_task(self, assigned_task_id=0, task_id=0, task_title="", assigned_user_id=0, assigned_username="", project_id=0):
        cursor = self.connection.cursor()
        updates = { "assigned_user_id": assigned_user_id, "assigned_username": assigned_username, "task_title": task_title }
        query = "UPDATE assigned_tasks SET " + ", ".join([f"{key} = {value}" if str(value).isdigit() and value != 0 else f"{key} = '{value}'" for key, value in updates.items() if value != ""])
        
        if assigned_task_id != 0:
            query += f" WHERE assigned_task_id = {assigned_task_id}"
        else:
            query += f" WHERE task_id = {task_id} AND assigned_user_id = {assigned_user_id} AND project_id = {project_id}"

        cursor.execute(query)
        self.connection.commit()
        return cursor.lastrowid

    def delete_user(self, user_id=0, username=""):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        DELETE FROM users
        WHERE username = '{username}' OR user_id = {user_id}
        """)
        self.connection.commit()
        return cursor.lastrowid

    def delete_project(self, project_id):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        DELETE FROM projects 
        WHERE project_id = {project_id}
        """)
        self.connection.commit()
        return cursor.lastrowid

    def delete_task(self, task_id=0, task_title="", project_id=0):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        DELETE FROM tasks 
        WHERE task_id = {task_id} OR (task_title = '{task_title}' AND project_id = {project_id})
        """)
        self.connection.commit()
        return cursor.lastrowid

    def remove_user_from_project(self, project_user_id=0, project_id=0, user_id=0, username=""):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        DELETE FROM project_users 
        WHERE project_user_id = {project_user_id} OR (project_id = {project_id} AND (user_id = {user_id} OR username = '{username}'))
        """)
        self.connection.commit()
        return cursor.lastrowid

    def remove_assigned_task(self, assigned_task_id=0, task_id=0, assigned_user_id=0, project_id=0):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        DELETE FROM assigned_tasks
        WHERE assigned_task_id = {assigned_task_id} OR (task_id = {task_id} AND assigned_user_id = {assigned_user_id} AND project_id = {project_id})
        """)
        self.connection.commit()
        return cursor.lastrowid

