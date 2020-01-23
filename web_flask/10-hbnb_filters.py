#!/usr/bin/python3
"""
starts a Flask web application
"""
import re
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters/', strict_slashes=False)
def only_states():
    """Displays an HTML page with a list of all States.
        States are sorted by name.
        and cities sorted by name.
        Amenities sorted by name..
        """
    all_states = storage.all('State')
    all_amenity = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=all_states,
                           amenities=all_amenity)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session.
    """
    storage.close()


if __name__ == '__main__':
    app.run()
