#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage, State
from models.state import State
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """comment"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('10-hbnb_filters.html', states=states)


@app.teardown_appcontext
def db_teardown(exception):
    """c"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
