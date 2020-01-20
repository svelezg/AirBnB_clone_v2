#!/usr/bin/python3
"""
starts a Flask web application
"""
import re
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    # display “C ” followed by the value of the text
    return 'C %s' % text.replace("_", " ")


if __name__ == '__main__':
    app.run()
