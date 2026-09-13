#!/usr/bin/python3
"""Convert JSON strings to python objects."""

import json


def from_json_string(my_str):
    """Return Python data structure from json string."""
    return json.loads(my_str)
