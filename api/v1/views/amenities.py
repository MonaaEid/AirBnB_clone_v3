#!/usr/bin/python3
"""view for State objects that handles all
default RESTFul API actions"""

from api.v1.views import app_views
from models import storage
from flask import request, jsonify, abort
from models.state import State
from models.city import City
from models.amenity import Amenity

