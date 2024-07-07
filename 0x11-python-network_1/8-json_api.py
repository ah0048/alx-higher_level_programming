#!/usr/bin/python3
'''takes in a letter and sends a POST request to url'''
import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    data = {'q': q}
    resp = requests.post(url, data=q)

    try:
        json_data = resp.json()
        if not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data['id'], json_data['name']))
    except ValueError:
        print('Not a valid JSON')
