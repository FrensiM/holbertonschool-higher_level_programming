#!/usr/bin/python3
'''reading text file'''


import json


def save_to_json_file(my_obj, filename):
    '''obj by json string'''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
