#!/usr/bin/python3
'''rectangle module'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if type(value) is not int:
            raise TypeError("height must be integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        if type(value) is not int:
            raise TypeError("x must be integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        if type(value) is not int:
            raise TypeError("y must be integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''method for area'''
        return self.width * self.height

    def display(self):
        '''method for printing rectangle'''
        print('\n' * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        '''print to user method'''
        return ("[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width,
            self.height
            ))

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle'''
        return self.__dict__
