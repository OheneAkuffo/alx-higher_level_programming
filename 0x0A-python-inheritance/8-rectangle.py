#!/usr/bin/python3
"""Class Module
A class Rectangle that inherits from BaseGeometry

Parameters:
    width (int) width of rectangle
    height (int) height of rectangle

Return:
    Always Nothing
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """SubClass of BaseGeometry
    """
    def __init__(self, width, height):
        """Intializes the object instance variable
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
