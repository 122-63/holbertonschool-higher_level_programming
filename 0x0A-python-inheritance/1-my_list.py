#!/usr/bin/python3
"""that prints the list"""


class MyList(list):
    """..."""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
