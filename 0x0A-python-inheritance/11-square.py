#!/usr/bin/python3
'''module for square class'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square class'''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''method for area'''
        return self.__size ** 2

    def __str__(self):
        '''method to print square'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
