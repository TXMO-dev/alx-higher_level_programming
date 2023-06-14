#!/usr/bin/python3
"""
append after the python
"""
def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a specific string"""
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(lines)
