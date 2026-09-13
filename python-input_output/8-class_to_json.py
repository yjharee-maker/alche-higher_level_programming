#!/usr/bin/python3
"""Return the dictionary description for JSON serialisation of an object."""


def class_to_json(obj):
    return obj.__dict__
