#!/usr/bin/python3
"""module as square"""


class Square:
    """class square with size verification"""
    def __init__(self, size=0):
        """constructor that checks value of size"""
        self.size = size

    @property
    def size(self):
        """property to return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter that checks value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
