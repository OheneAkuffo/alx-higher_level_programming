#!/usr/bin/python3
"""
    Defines the "append after" function
"""


def append_after(filename="", search_string="", new_string=""):
    """ appends "new_string"
        after a line containing
        "search_string" in "filename"
    """
    with open(filename, 'r', encoding='utf-8') as file:
        new_list = []
        while True:
            line = file.readline()
            if line == "":
                break
            new_list.append(line)
            if search_string in line:
                new_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(new_list)
