#!/usr/bin/python3
"""Return the dictionary description with a simple data structure for JSON serialisation of an object."""

def class_to_json(obj):
    return obj.__dict__
