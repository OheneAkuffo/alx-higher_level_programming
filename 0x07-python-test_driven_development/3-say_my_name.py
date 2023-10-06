#!/usr/bin/python3
"""
    A function that takes prints My name is
    <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """say_my_name takes in two arguments:
        Args:
            first_name (str): first name to printed
            last_name (str): second name to be printed
            with default empty string.
        Return:
            print out "My name is <first name> <last_name>
    """
    if not first_name and not last_name:
        raise TypeError("first_name must be a string")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
