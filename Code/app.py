from flask import Flask, request, jsonify, render_template
from use_database import *
import os
 
app = Flask(__name__)  # create a new Flask app
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/databaseConnect')
def databaseConnect():
    return render_template('dataScreen.html')
 
@app.route('/databaseCommand', methods=['POST'])
def databaseCommand():
    query = request.form['sqlQuery']
    print("Database Path:", os.path.abspath("database.db"))
    #get the path of the current working directory
    filepath = os.path.join(os.getcwd(), 'Code/database.db')
    print("File Path:", filepath)
    databaseConnection = create_connection(filepath)
    result = execute_query(databaseConnection, query)
    databaseConnection.close()
    return render_template('dataScreen.html', result=result)

@app.route('/supervisor')
def supervisor():
    return render_template('SupervisorHomePage.html')

app.run(port=5000)  # run the Flask app