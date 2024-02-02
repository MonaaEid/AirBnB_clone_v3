#!/usr/bin/python3
"""Module to define a flask blueprint"""
from api.v1.views import app_views
from flask import jsonify
import json
from models import storage

classes = {
    "amenities": "Amenity",
    "cities":'City',
    "places": 'Place',
    "reviews": 'Review',
    "states": 'State',
    "users": 'User'
}

@app_views.route("/status", strict_slashes=False)
def status():
    """return a json string"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    """retrieves the number of each objects by type"""
    stats = {}
    for key, value in classes.items():
        stats[key] = storage.count(value)
    return jsonify(stats)
