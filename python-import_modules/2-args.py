#!/usr/bin/python3

import sys

def print_arguments():
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 argument.")
        print(":")
    else:
        print("{} argument{}:".format(num_args, 's' if num_args > 1 else ''))
        for i, arg in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()
