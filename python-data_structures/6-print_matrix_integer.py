#!/usr/bin/python

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):


            print("{:d}".format(row[i]), end=" ")
            if (i + 1) % len(row) == 0 and row != matrix[-1]:
                print("")


            elif (i + 1) % len(row) == 0:
                print("")
                print("")





