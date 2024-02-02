#!/usr/bin/python3
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
    host = os.getenv("HBNB_API_HOST") if os.getenv("HBNB_API_HOST") else "0.0.0.0"
    port = os.getenv("HBNB_API_PORT") if os.getenv("HBNB_API_PORT") else 5000
    app.run(host=host, port=port, threaded=True)
    # app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
    # port=int(os.getenv('HBNB_API_PORT', 5000)),
    # threaded=True)