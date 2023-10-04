#!/usr/bin/python3
"""A class that prevent users from dynamically creating
    new instances
"""


class LockedClass:
    """ A locked class"""

    __slots__ = ["first_name"]
