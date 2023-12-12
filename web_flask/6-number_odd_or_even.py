#!/usr/bin/python3
"""
    This module contains a flask web app
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
                                    with <n> value in the html Body
                                    only if n is an integer
            /number_odd_or_even/<n>:    display a template
                                        with <n> value in the html Body
                                        and says if it is odd or even
                                        only if n is an integer
"""

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


if __name__ == '__main__':
    """
        The web application listen on
        0.0.0.0, port 5000 in debug mode
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
