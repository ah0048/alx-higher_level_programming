#!/usr/bin/python3
'''module for decoding json'''
import json


def from_json_string(my_str):
    '''function for decoding json'''
    return json.loads(my_str)
