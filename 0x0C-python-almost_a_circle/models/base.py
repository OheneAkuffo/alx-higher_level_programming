#!/usr/bin/python3
"""This class is the base of other classes"""

import json
import os
import csv
import turtle


class Base:
    """ Base class for all other classes
        Attributes:
            __nb_objects (int): The number of instantitated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Intantiates a new instance
            Args:
                id (int): the identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a Json representation
        Args:
            list_dictionaries (list): list containing values:
        Returns:
            json represation
        """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON representation to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """return the deserialize json string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instance from a dictionary of attribute"""
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
        else:
            tmp = cls(1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        If the file doesn't exit return an empty list
        otherwise a list of instances, must use from_json_string()
        and create(). Has the deserialization behaviour
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as open_file:
                json_data = open_file.read()
                dict_list = cls.from_json_string(json_data)
                dummy_instance = [cls.create(**d) for d in dict_list]
                return dummy_instance
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write the CSV serialization of list_objs to a file,
        Has the serialization behaviour
        """
        class_name = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            class_name = ["id", "size", "x", "y"]

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as open_file:
            writer = csv.DictWriter(open_file, fieldnames=class_name)
            if list_objs is None or list_objs == []:
                writer.write("[]")
            else:
                for objs in list_objs:
                    writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Mimicks the behavior of the JSON deserialization
        Return a list of classes from a CSV file
        """
        class_name = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            class_name = ["id", "size", "x", "y"]

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as open_file:
                l_d = csv.DictReader(open_file, fieldnames=class_name)
                dct = [dict([k, int(v)] for k, v in d.items()) for d in l_d]
                return [cls.create(**d) for d in dct]
        except IOError:
            return "[]"

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#7EC8E3")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#050A30")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#000C66")
        for square in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()
            for i in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
