#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    """Greet anyone who see this URL"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def greet2():
    """Greet anyone who see this URL"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def route_w_var(text):
    """Return abosulte path without slashes neither underscores"""
    return f'C {escape(text.replace("_", " "))}'


@app.route("/python/<text>", strict_slashes=False)
def python_w_var(text):
    """Return abosulte path without slashes neither underscores"""
    return f'Python {escape(text.replace("_", " "))}'


@app.route("/python", strict_slashes=False)
def python_default():
    """
    Return abosulte path without slashes neither
    underscores and a default value
    """
    return f'Python is cool'


@app.route("/number/<int:n>", strict_slashes=False)
def number_var(n):
    """Return abosulte path without slashes neither underscores"""
    return f'{escape(n)} is a number'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
