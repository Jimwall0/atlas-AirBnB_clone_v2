#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

# Set the app to listen on 0.0.0.0, port 5000
app.config["HOST"] = "0.0.0.0"
app.config["PORT"] = 5000

@app.teardown_appcontext
def teardown(exception):
    """Method to close the current SQLAlchemy session."""
    storage.close()

@app.route('/states_list')
def states_list():
    """Route that displays a list of states."""
    # Fetch all State objects sorted by name
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)

    # Render the template, passing the sorted states
    return render_template('states_list.html', states=sorted_states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
