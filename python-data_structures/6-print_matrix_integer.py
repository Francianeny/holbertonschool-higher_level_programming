#!/usr/bin/python

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Print each element followed by a space
            print("{:d}".format(row[i]), end=" ")
            # Check if the current column is the third one
            if (i + 1) % 3 == 0 and i != len(row) - 1:
             print(end="")
        print("")  # Move print("") outside the inner loop to print a new line after each row

