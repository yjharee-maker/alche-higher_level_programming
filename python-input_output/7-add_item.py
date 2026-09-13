#!/usr/bin/python3
"""Add command line arguments to a JSON file."""

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


"""Name of file."""
filename = "add_item.json"

"""Load existing list from JSON file."""
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    """If filename does not exist, return an empty list."""
    items = []

"""Add command line arguments except the script name."""
items.extend(sys.argv[1:])

"""Save the updated list to a JSON file."""
save_to_json_file(items, filename)
