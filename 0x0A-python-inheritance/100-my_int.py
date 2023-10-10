#!/usr/bin/python3
"""A class that Invert the meaning to the equal ==,
    and not equal != sign
"""


class MyInt(int):
    """Inherits form int"""
    def __init__(self, value):
        """Initialize instance attributes"""
        self.value = value

    def __eq__(self, other):
        """Invert the equal sign"""
        return (self.value != other)

    def __ne__(self, other):
        """Invert the not equal sign"""
        return (self.value == other)
