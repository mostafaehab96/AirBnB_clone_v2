#!/usr/bin/python3

"""Listing all states with /states_list route
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User


app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception):
    """Closes the session."""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def list_states():
    """Display list of states with cities and ameneties from database"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User)
    users = {key: f"{user.first_name}  {user.last_name}"
             for key, user in users.items()}
    return render_template("100-hbnb.html",
                           states=states,
                           amenities=amenities,
                           places=places,
                           users=users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
