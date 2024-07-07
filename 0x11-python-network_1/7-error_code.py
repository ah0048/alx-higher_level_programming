#!/usr/bin/python3
''' takes in a URL, sends a request to the URL and displays the body'''
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    resp = requests.get(url)
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
