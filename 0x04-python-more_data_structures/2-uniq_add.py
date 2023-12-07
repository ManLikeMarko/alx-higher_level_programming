#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    adds all unique integers in a list (only once for each integer).
    
    Args:
    my_list=[]: input list
    
    Returns:
    Sum of unique ints
    """
    unique_integers = set()
    total = 0

    for number in my_list:
        if number not in unique_integers:
            unique_integers.add(number)
            total += number

            return sum(set(my_list))
