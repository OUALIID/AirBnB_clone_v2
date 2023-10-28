#!/usr/bin/python3
"""Importing the flask module"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def HBNB():
    """A function that specifies the return value"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route for displaying 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display “C ” followed by the value of the text"""
    response = f"C {escape(text.replace('_', ' '))}"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
