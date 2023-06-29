#!/usr/bin/python3
'''firs class'''

import json
import os


class Base:
    '''Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        my_file = cls.__name__ + ".json"
        my_list = []
        if list_objs is not None:
            for el in list_objs:
                my_list.append(el.to_dictionary())

        with open(my_file, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(my_list))

    def from_json_string(json_string):
        if json_string is None or json_string is []:
            return []
        return json.loads(json_string)
