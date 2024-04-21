#!/usr/bin/python3
'''square module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''square method'''
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self.width = value
        self.height = value

    def __str__(self):
        '''print to user method'''
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width
            ))

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle'''
        attrs = ['id', 'size', 'x', 'y']
        dictionary = {}
        for attr in attrs:
            dictionary.update({attr: getattr(self, attr)})
        return dictionary
