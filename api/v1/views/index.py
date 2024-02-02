#!/usr/bin/env python3
from api.v1.views import app_views
from flask import jsonify
import json


@app_views.route("/status", method='GET')
def status():
    """return a json string"""
    return json({'status': 'OK'})