#!/usr/bin/python3
"""
    A Python script that takes in a URL,
    sends a request to the URL and displays the value of
    the X-Request-Id variable found in the header of the response.
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as response:
        body = response.headers.get("X-Request-Id")
        print(body)
