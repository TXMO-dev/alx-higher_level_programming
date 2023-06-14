#!/usr/bin/python3
"""
this loads json from file
"""
import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    
    Args:
        filename: The name of the JSON file.
    
    Returns:
        The object represented by the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

# Example usage
filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
