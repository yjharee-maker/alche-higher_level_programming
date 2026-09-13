#!/usr/bin/python3
"""Defines a function to add data in a file."""


def append_write(filename="", text=""):
    """Add 'text' in 'filename'."""

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
