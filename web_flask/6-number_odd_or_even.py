#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
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


@app.route("/number_template")
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n=0):
    """Return an HTML page showing the argument n"""
    return (render_template('5-number.html', number=escape(n)))


@app.route("/number_odd_or_even")
@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n=0):
    """Return an HTML page showing the argument n"""
    return (render_template('6-number_odd_or_even.html', number=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
