#!/usr/bin/python3
'''writing text file'''


def write_file(filename="", text=""):
    '''write func'''
    with open(filename, 'w', encoding="utf-8") as f:
        wr = f.write(text)
        return wr
