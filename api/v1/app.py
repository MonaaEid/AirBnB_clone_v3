#!/usr/bin/env python3
"""This module defines a Flask Blueprint."""
from flask import Flask
import json
from flask import redirect, render_template, request
import models
from api.v1.views import app_views
from models import storage, State
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def db_teardown(exception):
    """declare a method to handle @app.teardown_appcontext that calls storage.close()"""
    storage.close()


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
    port=int(os.getenv('HBNB_API_PORT', 5000)),
    threaded=True)