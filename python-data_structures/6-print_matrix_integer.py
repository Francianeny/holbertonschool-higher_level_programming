#!/usr/bin/python

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print("")# Move to the next line after printing each row



