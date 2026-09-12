#!/usr/bin/python3
"""Defines a function to put data in a file."""


def write_file(filename="", text=""):
    """Write 'text' in 'filename'."""

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
