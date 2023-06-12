#!/usr/bin/python3
"""
Defines an add_attribute function that adds a new attribute to an object if possible.
"""

def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.
    Args:
        obj (object): The object to add the attribute to.
        attribute (str): The name of the attribute.
        value (any): The value of the attribute.
    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)


# Test case
if __name__ == "__main__":
    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
