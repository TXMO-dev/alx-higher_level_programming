#!/usr/bin/python3
"""
this is the is kind of class implementation
"""
def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or its subclasses.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
