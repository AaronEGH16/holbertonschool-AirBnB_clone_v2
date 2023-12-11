#!/usr/bin/python3
"""
    This module contains a flask web app
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


if __name__ == '__main__':
    """
        The web application listen on
        0.0.0.0, port 5000 in debug mode
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
