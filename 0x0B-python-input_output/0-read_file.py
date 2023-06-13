#!/usr/bin/python3
"""
this si the read file assignemnt.
"""
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.
    
    Args:
        filename (str): The name of the file to read.
            Defaults to an empty string.
    """
    with open(filename, 'r') as file:
        content = file.read()  # Read the content of the file
    print(content)  # Print the content to stdout

read_file("my_file_0.txt")
