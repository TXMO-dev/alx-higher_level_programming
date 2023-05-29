#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Counter for the number of elements printed

    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass  # Ignore index errors if x is greater than the length of my_list

    print()  # Print a new line after all elements are printed
    return count
