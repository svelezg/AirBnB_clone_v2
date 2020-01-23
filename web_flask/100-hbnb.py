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


@app.route('/hbnb/', strict_slashes=False)
def only_states():
    """Displays an HTML page with a list of all States.
        States are sorted by name.
        """
    all_states = storage.all('State')
    all_amenity = storage.all('Amenity')
    all_places = storage.all('Place')
    all_users = storage.all('User')
    return render_template('100-hbnb.html',
                           states=all_states,
                           amenities=all_amenity,
                           places=all_places,
                           users=all_users)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session.
    """
    storage.close()


if __name__ == '__main__':
    app.run()
