from flask import Flask, request, jsonify, render_template

app = Flask(__name__)  # create a new Flask app

@app.route('/')
def index():
    return render_template('index.html')

app.run(port=5000)  # run the Flask app