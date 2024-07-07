#!/usr/bin/python3
'''sends a request to the URL and displays the value of the variable X-Request-Id'''
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    resp = requests.get(url)
    print(resp.headers['X-Request-Id'])
