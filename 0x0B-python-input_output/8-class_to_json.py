#!/usr/bin/python3
'''returns the dictionary description with simple data structure'''
import json


def class_to_json(obj):
    '''function for dictionary'''
    return obj.__dict__
