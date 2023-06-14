#!/usr/bin/python3
"""Module to convert objects to JSON-serializable dictionaries"""

def class_to_json(obj):
    """Converts an object to a JSON-serializable dictionary"""

    # Create an empty dictionary to store the serialized data
    json_data = {}

    # Get the attributes of the object
    attributes = obj.__dict__

    # Iterate through each attribute
    for key, value in attributes.items():
        # Check the type of the attribute
        if isinstance(value, (list, dict, str, int, bool)):
            # If it's a serializable type, add it to the dictionary
            json_data[key] = value

    return json_data
