#!/usr/bin/python3

"""Listing all states with /states_list route
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
states = storage.all(State).values()


@app.teardown_appcontext
def close_db(exception):
    """Closes the session."""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    """Display list of states in database."""
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def list_state_cities():
    """Display state with it's corresponding cities"""
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)