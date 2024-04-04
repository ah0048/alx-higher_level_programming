#!/usr/bin/python3
"""module as square"""


class Square:
    """class square with size verification"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor that checks value of size"""
        self.size = size
        self.position = position

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

    def area(self):
        """method to calculate square area"""
        return self.__size * self.__size

    @property
    def position(self):
        """property to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """method to print a square"""
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(1, self.__size + 1):
            for z in range(self.__position[0]):
                print(" ", end="")
            print("#" * self.__size)
