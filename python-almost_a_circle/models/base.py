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

    @property
    def to_json_string(list_dictionaries):
        '''fun that return json presentation'''
        if list_dictionaries is None:
            return []
        else:
            return json.loads(list_dictionaries)
