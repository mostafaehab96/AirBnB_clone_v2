#!/usr/bin/python3

"""Listing all states with /states_list route
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception):
    """Closes the session."""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    """Display list of states in database."""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
