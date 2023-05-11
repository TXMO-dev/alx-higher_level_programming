#!/usr/bin/python3

# Import specific functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Assign values to variables a and b
a = 10
b = 5

# Call each imported function with a and b as arguments and print the result
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
