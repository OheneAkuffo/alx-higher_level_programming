#!/usr/bin/python3
"""Function that append string to a file"""


def write_file(filename="", text=""):
    """Return the number of text written to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
