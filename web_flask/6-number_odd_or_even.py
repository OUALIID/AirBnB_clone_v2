#!/usr/bin/python3
"""Importing the flask module"""

from flask import Flask, escape, render_template

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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ display “Python ”, followed by the value of the text"""
    response = f"Python {escape(text.replace('_', ' '))}"
    return response


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', Number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        result = "even"
    else:
        result = "odd"
    file = '6-number_odd_or_even.html'
    return render_template(file, Number=n, Result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
