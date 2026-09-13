#!/usr/bin/python3
"""Convert python objects to JSON strings."""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object."""
    return json.dumps(my_obj)
