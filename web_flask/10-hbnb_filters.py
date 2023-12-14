#!/usr/bin/python3
"""
    This module contains a Flask web app
    that starts on 0.0.0.0:5000
    routes:
        /:  display "Hello HBNB!"
        /hbnb:  display "HBNB"
        /c/<text>:  display "C " followed by
                    text converting "_" to spaces
        /python/<text>: display "Python " followed by
                        text converting "_" to spaces
                        (default text value is "is cool")
        /number/<n>:    display "<n> is a number" only
                        if n is an integer
        /number_template/<n>:   display a template
                                with <n> value in the HTML Body
                                only if n is an integer
        /number_odd_or_even/<n>:    display a template
                                    with <n> value in the HTML Body
                                    and say if it is odd or even
                                    only if n is an integer
        /states_list:   display a template with a list of states
        /cities_by_states:  display a template witha a list of cities by states
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    mod_text = "".join([" " if letter == "_" else letter for letter in text])
    return f"C {mod_text}"


@app.route("/python")
@app.route("/python/<text>")
def python(text="is cool"):
    mod_text = "".join([" " if letter == "_" else letter for letter in text])
    return f"Python {mod_text}"


@app.route("/number/<int:n>")
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n)


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route("/states_list")
def states_list():
    obj_list = storage.all("State")
    return render_template("7-states_list.html", obj_list=obj_list)


@app.route("/cities_by_states")
def cities_by_states():
    obj_list = storage.all("State")
    return render_template("8-cities_by_states.html", obj_list=obj_list)


@app.route("/states/")
@app.route("/states/<id>")
def states(id=None):
    obj_list = storage.all("State")
    state_id = f"State.{id}"
    return render_template("9-states.html", obj_list=obj_list, id=state_id)


@app.route("/hbnb_filters")
def hbnb_filters():
    state_list = storage.all("State")
    amenity_list = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           obj_list=state_list, amenity=amenity_list)


if __name__ == '__main__':
    """
    The web application listens on
    0.0.0.0, port 5000 in debug mode
    """
    app.run(host='0.0.0.0', port=5000, debug=False)
