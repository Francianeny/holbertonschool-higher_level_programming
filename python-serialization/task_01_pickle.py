#!/usr/bin/python3
"""contains the Pickling Custom Classes"""


import pickle


class CustomObject:
    """custom class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """ method display """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Is Student: {self.is_student}")
