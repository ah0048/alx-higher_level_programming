#!/usr/bin/python3
'''sends a request to the URL and displays the value of the X-Request-Id'''
from urllib import request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as resp:
        header = resp.headers
        print(header['X-Request-Id'])
