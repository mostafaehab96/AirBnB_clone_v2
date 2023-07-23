#!/usr/bin/python3

"""Listing all states with /states_list route
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception):
    """Closes the session."""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def list_states():
    """Display list of states with cities and ameneties from database"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html",
                           states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
