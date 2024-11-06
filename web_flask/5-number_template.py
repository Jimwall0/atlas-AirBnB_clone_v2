#!/usr/bin/python3
"""Make a flask application"""
from flask import Flask, render_template


app = Flask("__name__")


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index2():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def index3(text):
    return "C %s" % text.replace("_", " ")


@app.route("/python/", strict_slashes=False)
def index4_1():
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def index4_2(text="is_cool"):
    return "Python %s" % text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def index5(n):
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def index6(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
