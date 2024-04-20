#!/usr/bin/python3
'''square module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''square method'''
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''print to user method'''
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width
            ))
