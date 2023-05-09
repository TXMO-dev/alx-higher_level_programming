#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - (ord('a') - ord('A')))
        else:
            result += char

    print(result)
