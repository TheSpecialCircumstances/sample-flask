from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/hi")
def hi():
    return '<h3>This is a Flask web application.</h3>'