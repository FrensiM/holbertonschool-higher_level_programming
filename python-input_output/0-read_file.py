#!/usr/bin/python3
'''reading text file'''


def read_file(filename=""):
    '''readung file'''
    with open(filename, "r", encoding="utf-8") as f:
        fr = f.read()
        print(fr, end='')
