#!/usr/bin/python3
"""
    A Python script that takes in a letter and sends a POST
    request to http://0.0.0.0:5000/search_user with the letter
    as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    try:
        q = argv[1]
    except Exception:
        q = ""
    value = {'q': q}
    response = requests.post(url, value)
    try:
        json_response = response.json()
        if json_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_response["id"], json_response["name"]))
    except ValueError:
        print("Not a valid JSON")
