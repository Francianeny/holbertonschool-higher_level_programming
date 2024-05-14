#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two integers from each tuple or use 0 for missing elements
    a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    b = tuple_b[:2] + (0,) * (2 - len(tuple_b))

    # Add corresponding elements together
    result = (a[0] + b[0], a[1] + b[1])

    return result
