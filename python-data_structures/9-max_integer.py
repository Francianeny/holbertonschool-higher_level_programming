#!/usr/bin/python3

def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    # Initialize the maximum integer with the first element of the list
    max_num = my_list[0]

    # Iterate through the list to find the maximum integer
    for num in my_list:
        if num > max_num:
            max_num = num

            return max_num
