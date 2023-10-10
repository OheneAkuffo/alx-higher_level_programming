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

    def integer_validator(self, name, value):
        """ Raises TypeError if value is not Integer;
            Raises ValueError if value is less than 0
        """

        if type(value) is not int:

            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
