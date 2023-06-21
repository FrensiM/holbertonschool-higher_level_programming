#!/usr/bin/python3
import json
'''reading text file'''


def to_json_string(my_obj):
    '''jason to str fun'''
    json_repr = json.dumps(my_obj)
    return json_repr
