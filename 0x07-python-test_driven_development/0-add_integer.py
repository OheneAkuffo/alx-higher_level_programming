#!/usr/bin/python3
""" A function definition that add two numbers together
    The add function takes two args and add them together
    Args:
        a (int): should be an interger
        b (int): should be an integer
    Return:
        the sum of (a) and (b)
"""


def add_integer(a, b=98):
    """A functions that add two number"""

    if (type(a) is not float) and (type(a) is not int):
        raise TypeError("a must be an integer")
    if (type(b) is not float) and (type(b) is not int):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (a) + (b)
