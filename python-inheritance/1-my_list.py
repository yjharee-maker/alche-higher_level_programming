#!/usr/bin/python3
"""Define MyList class."""


class MyList(list):
    """Subclass of list to print sorted lists."""

    def print_sorted(self):
        """Print sorted list in ascending order."""
        print(sorted(self))
