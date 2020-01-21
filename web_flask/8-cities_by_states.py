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


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


@app.route('/cities_by_states/', strict_slashes=False)
def cities_by_state():
    all_states = storage.all('State')
    #for state in all_states.values():
     #   for city in state.cities:
      #      print(city.name)
    return render_template('8-cities_by_states.html', states=all_states)


if __name__ == '__main__':
    app.run()
