#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Print each element followed by a space
            print("{:d}".format(row[i]), end=" ")
            print() # Move to the next line after printing each row
