#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except Exception as err:
        error = "Exception: " + str(err) + "\n"
        sys.stderr.write(error)
        return (None)
