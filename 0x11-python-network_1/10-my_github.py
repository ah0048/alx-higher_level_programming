#!/usr/bin/python3
'''takes in a letter and sends a POST request to url'''
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = argv[1]
    passwrd = argv[2]
    resp = requests.get(url, auth=(user, passwrd))
    if resp.status_code == 200:
        print(resp.json()['id'])
    else:
        print('None')
