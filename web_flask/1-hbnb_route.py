#!/usr/bin/python3
"""
    This module contains a flask web app
    that starts on 0.0.0.0:5000
        routes:
            /:      display "Hello HBNB!"
            /hbnb:  display "HBNB"
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


if __name__ == '__main__':
    """
        The web application listen on
        0.0.0.0, port 5000 in debug mode
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
