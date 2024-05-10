#!/usr/bin/python3

def uppercase(s):
    for char in s:
        upper_char = chr(ord(char) - 32) if 65 <= ord(char) <= 90 else char
        print(upper_char, end="")
    print()
