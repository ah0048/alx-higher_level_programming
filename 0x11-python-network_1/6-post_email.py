#!/usr/bin/python3
'''sends a POST request to the passed URL with the email as a parameter'''
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    resp = requests.post(url, data=data)
    print(resp.text)
