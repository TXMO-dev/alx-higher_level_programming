#!/usr/bin/python3
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Check if the JSON file exists
if path.exists(filename):
    # Load existing data from the JSON file
    data = load_from_json_file(filename)
else:
    # Create an empty list if the file doesn't exist
    data = []

# Add command-line arguments to the list
data.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(data, filename)

