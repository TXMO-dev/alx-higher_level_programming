#!/usr/bin/python3
"""
this si the append write file"
"""
def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.
    
    If the file doesn't exist, it will be created.
    
    Args:
        filename (str): The name of the file to append to.
            Defaults to an empty string.
        text (str): The string to append to the file.
            Defaults to an empty string.
    
    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a') as file:
        count = file.write(text)  # Append the text to the file and get the character count
    return count

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
