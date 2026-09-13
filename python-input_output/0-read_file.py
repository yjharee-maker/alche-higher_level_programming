#!/usr/bin/python3
"""Defines a function that opens a file, reads it, prints it, and closes it."""


def read_file(filename=""):
    """Open a file, read it, print it, close it."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
