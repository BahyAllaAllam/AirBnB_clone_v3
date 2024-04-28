#!/usr/bin/python3
"""
Index file for setting up th api
"""

from flask import jsonify
from . import app_views
from models import storage


classes = {"users": "User",
           "places": "Place",
           "states": "State",
           "cities": "City",
           "amenities": "Amenity",
           "reviews": "Review"}


@app_views.route('/status', strict_slashes=False)
def status():
    """Returns the status in json format."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """Returns count of all objs in json format."""
    count_objs = {}
    for key, value in classes.items():
        count_objs[key] = storage.count(value)
    return jsonify(count)
