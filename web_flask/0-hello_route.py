#!/usr/bin/python3 Flask
""" This is a program to print a simple message """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """This is a simple program to print "Hello HBNB!" on a webpage"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
