#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    # display “C ” followed by the value of the text
    return 'C %s' % text.replace("_", " ")


@app.route('/python/', strict_slashes=False, defaults={"text": "is cool"})
@app.route('/python/<text>')
def show_python(text):
    # display “Python ”, followed by the value of the text
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    # display “n is a number” only if n is an integer
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    # display “n is a number” template
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
