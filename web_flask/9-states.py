#!/usr/bin/python3
"""
starts a Flask web application
"""
import re
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from collections import OrderedDict

app = Flask(__name__)


@app.route('/states/', strict_slashes=False)
def only_states():
    """Displays an HTML page with a list of all States.
        States are sorted by name.
        """
    all_states = storage.all('State')
    return render_template('9-states.html', states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def state_and_cities(id):
    """Displays an HTML page with info about <id>, if it exists.
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session.
    """
    storage.close()


if __name__ == '__main__':
    app.run()
