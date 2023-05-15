#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extend tuples to have at least 2 elements by appending 0s
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Get the sum of the first two elements from each tuple
    sum_first = tuple_a[0] + tuple_b[0]
    sum_second = tuple_a[1] + tuple_b[1]

    # Create a new tuple with the sums
    new_tuple = (sum_first, sum_second)
    return new_tuple
