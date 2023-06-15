#!/usr/bin/python3
""" Integer addition module """


def print_square(size):
    '''printing a square'''
    if type(size) is str:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for el in range(size):
        for elem in range(size):
            print("#", end="")
        print()
