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
        '''json str'''
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''func that save'''
        my_file = cls.__name__ + ".json"
        my_list = []
        if list_objs is not None:
            for el in list_objs:
                my_list.append(el.to_dictionary())

        with open(my_file, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(my_list))

    def from_json_string(json_string):
        '''json'''
        if json_string is None or json_string is []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_ins = cls(1, 2, 3, 4)
        else:
            dummy_ins = cls(2, 3, 4)

        dummy_ins.update(**dictionary)

        return dummy_ins

    @classmethod
    def load_from_file(cls):
        my_list = []
        myfile = cls.__name__ + ".json"
        if not os.path.exists(myfile):
            return []
        with open(myfile, 'r', encoding="utf-8") as f:
            dicto = cls.from_json_string(f.read())
            print(dicto)
            for obj in dicto:
                my_list.append(cls.create(**obj))

            return my_list
