#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry(object):
    """An empty class"""
    def __init__(self):
        """Initial empty intances variable"""
        pass

    def area(self):
        """Raises an exception when called"""
        raise Exception("area() is not implemented")
