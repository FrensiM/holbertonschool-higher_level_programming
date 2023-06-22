#!/usr/bin/python3
'''reading text file'''


import json


def from_json_string(my_str):
    '''obj by json string'''
    return json.loads(my_str)
