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
    def load_from_file(cls):
        '''file load'''
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

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves dictionary repr to json file"""
        filename = '{}.json'.format(cls.__name__)
        ls = []
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write(json.dumps(ls))
            else:
                for elem in list_objs:
                    class_dict = cls.to_dictionary(elem)
                    ls.append(class_dict)
                f.write(Base.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """Turns a string to a python object"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new object"""
        if cls.__name__ == 'Rectangle':
            new_obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """Gets a list of objects from json file"""
        filename = '{}.json'.format(cls.__name__)
        ls = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                obj_json_string = f.read()
            obj_ls = cls.from_json_string(obj_json_string)
            for elem in obj_ls:
                obj = cls.create(**elem)
                ls.append(obj)
        return ls
