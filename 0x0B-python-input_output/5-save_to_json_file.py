#!/usr/bin/python3
"""
this saves json to file
"""
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.
    
    Args:
        my_obj: The object to be saved to the file.
        filename: The name of the file to write the JSON representation to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

# Example usage
filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = {
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = {132, 3}
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
