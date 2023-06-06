#!/usr/bin/python3
"""
This module defines a Square class.
"""
def magic_string():
    """
    This module defines a Square class.
    """
    magic_string.count = getattr(magic_string, 'count', -1) + 1
    return "BestSchool" + ", BestSchool" * magic_string.count
