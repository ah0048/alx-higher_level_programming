#!/usr/bin/python3
'''takes in a URL and an email, sends a POST request to the passed URL'''
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as resp:
            body = resp.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
