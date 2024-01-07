#!/usr/bin/python3
"""
    Print out commit messages from github
"""
from sys import argv
import requests


if __name__ == "__main__":
    repo_name = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo_name)
    response = requests.get(url)
    count = 0
    try:
        for commit in response.json():
            if count == 10:
                break
            author = commit.get("commit").get("author")
            print("{}: {}".format(commit.get("sha"), author.get("name")))
            count += 1
    except IndexError:
        pass
