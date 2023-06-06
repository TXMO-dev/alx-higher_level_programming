#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = [".", "?", ":"]
    result = ""
    current_line = ""

    for char in text:
        current_line += char

        if char in special_chars:
            result += current_line.strip() + "\n\n"
            current_line = ""

    if current_line:
        result += current_line.strip()

    print(result)

