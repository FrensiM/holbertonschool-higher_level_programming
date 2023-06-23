#!/usr/bin/python3
'''module to create a JSON file'''


import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.exists("add_item.json") is not True:
    with open("add_item.json", "w", encoding='utf-8') as file:
        my_list = []
        save_to_json_file(my_list, "add_item.json")
my_list = load_from_json_file('add_item.json')
for i in range(len(sys.argv)):
    if i != 0:
        my_list.append(sys.argv[i])
save_to_json_file(my_list, 'add_item.json')
