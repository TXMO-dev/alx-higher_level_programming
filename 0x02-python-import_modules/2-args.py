#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1

if num_args == 0:
    print("{} arguments.".format(num_args))
else:
    if num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
