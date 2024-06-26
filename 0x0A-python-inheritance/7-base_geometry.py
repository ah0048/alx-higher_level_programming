#!/usr/bin/python3
'''module for BaseGeometry class'''


class BaseGeometry:
    '''class base geometry'''
    def area(self):
        '''method for area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''method for validation'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
