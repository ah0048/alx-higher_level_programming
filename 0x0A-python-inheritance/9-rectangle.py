#!/usr/bin/python3
'''module for BaseGeometry class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''subclass from base geometry'''
    def __init__(self, width, height):
        '''constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''method to get area'''
        return self.__height * self.__width

    def __str__(self):
        '''ethod to print Rectangle'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
