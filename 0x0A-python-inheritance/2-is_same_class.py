#!/usr/bin/python3
'''module for is_same_class method'''


def is_same_class(obj, a_class):
    ''' returns True if the object is an instance of the specified class'''
    return type(obj) is a_class
