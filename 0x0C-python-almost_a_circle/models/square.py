#!/usr/bin/python3

"""This module defines the Square Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """getter/setter for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square values:
        Args:
            *args (ints): New tuple attribute values
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        count = 0
        if len(args) != 0:
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1

        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__int__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Dictionary representation of the Square with key/value"""
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}

    def __str__(self):
        """return the print() representation of the Square class"""
        square = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                   self.width)
        return square
