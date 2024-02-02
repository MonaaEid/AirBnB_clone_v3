#!/usr/bin/python3
"""Module to define a flask blueprint"""
from api.v1.views import app_views
from flask import jsonify
import json


@app_views.route("/status", strict_slashes=False)
def status():
    """return a json string"""
    return jsonify({'status': 'OK'})