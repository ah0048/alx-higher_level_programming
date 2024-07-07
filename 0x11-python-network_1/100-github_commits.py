#!/usr/bin/python3
'''list 10 commits'''
import requests
from sys import argv


if __name__ == "__main__":
    user = argv[2]
    repo = argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)
    resp = requests.get(url)
    json_data = resp.json()
    try:
        for i in range(0, 10):
            print("{}: {}".format(json_data[i]['sha'],
                                  json_data[i]['commit']['author']['name']))
    except IndexError:
        pass
