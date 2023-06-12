#!/usr/bin/python3
"""another square module"""


class Square:
    '''init gfunc'''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')

        elif size < 0:
            raise ValueError('size must be >= 0')

        else:
            self.__size = size

    '''getting size'''
    @property
    def size(self):
        return self.__size

    '''changing size func'''
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

        '''find area of square'''
    def area(self):
        return self.__size ** 2
