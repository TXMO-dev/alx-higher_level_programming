#!/usr/bin/python3i

def remove_char_at(string, n):
    if n >= len(string) or n < 0:
        return string

    new_string = ""
    for i in range(len(string)):
        if i != n:
            new_string += string[i]

    return new_string
