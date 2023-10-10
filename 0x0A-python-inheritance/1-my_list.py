#!/usr/bin/python3
"""A class that Inherits from list"""


class MyList(list):
    """Class that defines my list"""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
