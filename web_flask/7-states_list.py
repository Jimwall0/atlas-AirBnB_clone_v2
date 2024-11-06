#!/usr/bin/python3
""" Make a Flask script """
from flask import Flask, render_template
import models


app = Flask(__name__)


@app.teardown_appcontext
def storage_close():
    """Removes the current Sqlalchemy session"""
    models.storage.close()



@app.route("/states_list", strict_slashes=False)
def index():
    states = models.storage.all(models.state)
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", state=states_sorted)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
