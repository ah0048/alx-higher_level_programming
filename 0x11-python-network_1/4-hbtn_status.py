#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    resp = requests.get(url)
    data = resp.text
    print('Body response:')
    print('\t- type: {}'.format(type(data)))
    print('\t- content: {}'.format(data))
