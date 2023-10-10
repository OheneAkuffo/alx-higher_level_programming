#!/usr/bin/python3
"""A function that returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """Takes in object and and return return it attributes and
        method
        Args:
            obj (obj): object
        Return: Always Nothing
    """

    return (dir(obj))
