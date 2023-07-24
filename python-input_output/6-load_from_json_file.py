#!/usr/bin/python3
'''reading text file'''


import json


def load_from_json_file(filename):
    '''creating obj'''
    with open(filename, 'r', encoding='utf-8') as f:
        obj = f.read()
        return json.loads(obj)
