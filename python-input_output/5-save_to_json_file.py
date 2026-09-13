#!/usr/bin/python3
"""Save Python objects as JSON."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object in a file using JSON representation."""
    with open(filename, "w") as f:
        json.dumps(my_obj, f)
