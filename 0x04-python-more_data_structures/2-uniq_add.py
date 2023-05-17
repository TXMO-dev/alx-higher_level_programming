#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_set = set()
    
    # Iterate over the list and add unique integers to the set
    for num in my_list:
        unique_set.add(num)
    
    # Sum all the integers in the set and return the result
    return sum(unique_set)
