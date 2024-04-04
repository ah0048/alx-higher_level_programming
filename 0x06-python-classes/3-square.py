#!/usr/bin/python3
"""module as square"""


class Square:
    """class square with size verification"""
    def __init__(self, size=0):
        """constructor that checks value of size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """method to calculate square area"""
        return self.__size * self.__size
