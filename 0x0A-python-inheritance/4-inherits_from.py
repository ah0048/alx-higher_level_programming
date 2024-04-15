#!/usr/bin/python3
'''module for inherits_from'''


def inherits_from(obj, a_class):
    '''checks if the object is an instance of a subclass'''
    return isinstance(obj, a_class) and type(obj) != a_class
