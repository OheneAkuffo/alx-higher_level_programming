#!/usr/bin/python3
"""A functon that returns True if the object is exactly
    and instance of the specified class
    otherwise false
"""


def is_same_class(obj, a_class):
    """a class that check class type:

    is_same_class (func): check class type

    Return: True if exact, else False
    """
    return (type(obj) == a_class)
