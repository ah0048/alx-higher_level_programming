#!/usr/bin/python3
'''module for student class'''


class Student:
    '''defines a student'''

    def __init__(self, first_name, last_name, age):
        '''constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieves a dictionary representation'''
        return self.__dict__
