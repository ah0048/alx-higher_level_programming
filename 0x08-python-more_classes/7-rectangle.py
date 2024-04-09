#!/usr/bin/python3
''' module for rectangle class'''


class Rectangle:
    ''' rectangle class'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''initialization instance'''
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''method to calculate area'''
        return self.__height * self.__width

    def perimeter(self):
        '''method to calculate perimeter'''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        '''method to print rectangle'''
        if self.__height == 0 or self.__width == 0:
            return ""
        symbol = str(self.print_symbol)
        return '\n'.join([symbol * self.__width] * self.__height)

    def __repr__(self):
        '''method to return string representation of the rectangle'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''method to print message when deleting obj'''
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
