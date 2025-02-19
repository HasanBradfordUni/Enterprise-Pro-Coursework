import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    query = """
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'User',
        team TEXT
    );
    """
    
    execute_query(connection, query)

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        return cursor.fetchall()
    except Error as e:
        return f"The error '{e}' occurred"