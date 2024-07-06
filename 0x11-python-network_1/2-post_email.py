#!/usr/bin/python3
'''takes in a URL and an email, sends a POST request to the passed URL'''
from urllib import request
from urllib import parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    encoded_data = parse.urlencode(data)
    req = request.Request(url, encoded_data)
    with request.urlopen(url) as resp:
        body = resp.read().encode('utf-8')
        print(body)
