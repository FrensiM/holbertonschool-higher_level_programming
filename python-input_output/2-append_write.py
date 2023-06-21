#!/usr/bin/python3
'''reading text file'''


def append_write(filename="", text=""):
    '''apending at the end func'''
    with open(filename, 'a', encoding="utf-8") as f:
        fn = f.write(text)
    return fn
