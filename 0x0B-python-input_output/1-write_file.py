#!/usr/bin/python3
"""
this si the write file
"""
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.
    
    Args:
        filename (str): The name of the file to write to.
            Defaults to an empty string.
        text (str): The string to write to the file.
            Defaults to an empty string.
    
    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w') as file:
        count = file.write(text)  # Write the text to the file and get the character count
    return count

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
