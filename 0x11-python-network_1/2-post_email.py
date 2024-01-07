#!/usr/bin/python3
"""
    A Python script that takes in a URL and an email, sends a POST
    request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    url = argv[1]

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
        print(body)
