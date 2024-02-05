#!/usr/bin/python3
"""This module start Flask application"""
from api.v1.views import app_views
from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def db_teardown(code):
    """declare a method to handle @app.teardown_appcontext
    that calls storage.close()"""
    storage.close()


@app.errorhandler(404)
def not_found(self):
    """ handle 404 error(not found)"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    # app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
    #         port=int(os.getenv('HBNB_API_PORT', '5000')),
    #         threaded=True)

    host = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else "0.0.0.0"
    port = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else 5000
    app.run(host=host, port=port, threaded=True)