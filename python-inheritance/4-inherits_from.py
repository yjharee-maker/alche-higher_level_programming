#!/usr/bin/python3
"""Checking class inheritance."""


def inherits_from(obj, a_class):
    """If object isinstance of a subclass of a_class."""

    return isinstance(obj, a_class) and type(obj) is not a_class
