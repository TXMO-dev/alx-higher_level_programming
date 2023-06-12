#!/usr/bin/python3
"""
this is the my list of everything.
"""
class MyList(list):
    """A custom list class that prints the list, but sorted in ascending order."""

    def print_sorted(self):
        """Print the list in sorted (ascending) order."""
        sorted_list = sorted(self)
        print(sorted_list)
