#!/usr/bin/python3
"""A function that prints a square with the character #"""


def print_square(size):
    """print the square with the character #
    Args:
        size (int): the size of the square to be printed
        and it should not be less than zerro:
    Return:
    Always Nothing
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for m in range(size):
        for n in range(size):
            print("#", end="")
        print()
