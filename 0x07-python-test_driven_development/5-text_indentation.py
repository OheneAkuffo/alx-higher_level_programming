#!/usr/bin/python3
""" A function that prints a text with 2 new lines after
    each of these characters ".", "?" and ":"
"""


def text_indentation(text):
    """This function takes str(text) to be printed out
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    state = 0
    for char in text:
        if state == 0:
            if char == " ":
                continue
            else:
                state = 1
        if state == 1:
            if char == "." or char == "?" or char == ":":
                print(char)
                print()
                state = 0
            else:
                print(char, end="")
