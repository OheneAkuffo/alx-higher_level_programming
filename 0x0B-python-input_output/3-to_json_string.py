#!/usr/bin/python3
"""returns the JSON representation of an object"""


import json


def to_json_string(my_obj):
    """return the JSON representation if an object"""
    return json.dumps(my_obj)
