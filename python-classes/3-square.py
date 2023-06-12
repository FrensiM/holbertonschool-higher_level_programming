#!/usr/bin/python3
"""another square module"""


class Square:
    '''init gfunc'''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
    def area(self):
        if self.area:
            print(f"{self.__size ** 2}")