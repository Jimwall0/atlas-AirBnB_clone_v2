#!/usr/bin/python3
"""A simple Flask web application for AirBnB clone project"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route handler for the root URL, displays a welcome message"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
