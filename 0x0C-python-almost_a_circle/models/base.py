#!/usr/bin/python3
'''base module'''
import json


class Base:
    '''base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''constuctor method'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        if list_objs is None:
            list_objs = []
        else:
            list_objs = [inst.to_dictionary() for inst in list_objs]
        filename = "{}.json".format(cls.__name__)
        json_text = cls.to_json_string(list_objs)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_text)

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation'''
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            obj = Rectangle(1, 1)
        elif cls is Square:
            obj = Square(1)
        else:
            obj = None
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf-8") as f:
                list_dict = cls.from_json_string(f.read())
                list_objs = []
                for dictionary in list_dict:
                    obj = cls.create(**dictionary)
                    list_objs.append(obj)
                return list_objs
        except FileNotFoundError:
            return []
