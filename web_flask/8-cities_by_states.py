#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(san):
    """Remove the current SQLAlchemy session."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    all_states = storage.all('State')
    return render_template('8-cities_by_states.html', states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
