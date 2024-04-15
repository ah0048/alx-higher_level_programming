#!/usr/bin/python3
'''module for inherits_from'''


def inherits_from(obj, a_class):
    '''checks if the object is an instance of a subclass'''
    return False if type(obj) is a_class else isinstance(obj, a_class)
