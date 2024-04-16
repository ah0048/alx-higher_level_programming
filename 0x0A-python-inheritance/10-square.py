#!/usr/bin/python3
'''module for square class'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square class'''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
    def area(self):
        return self.__size ^ 2
