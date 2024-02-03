#!/usr/bin/python3
"""This module start Flask application"""
from flask import Flask, jsonify, Blueprint
from api.v1.views import app_views
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def db_teardown(self):
    """declare a method to handle @app.teardown_appcontext
    that calls storage.close()"""
    storage.close()


@app.errorhandler(404)
def not_found(self):
    """ handle 404 error(not found)"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST") if os.getenv(
        "HBNB_API_HOST") else "0.0.0.0"
    port = os.getenv("HBNB_API_PORT") if os.getenv("HBNB_API_PORT") else 5000
    app.run(host=host, port=port, threaded=True)
    # app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
    #         port=int(os.getenv('HBNB_API_PORT', 5000)),
    #         threaded=True)
