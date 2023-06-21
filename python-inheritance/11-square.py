#!/usr/bin/python3
'''Module for a func'''


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    '''subclass'''
    def __init__(self, size):
        '''initialization'''
        BaseGeometry.integer_validator(self, 'size', size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        '''area of square'''
        return self.__size * self.__size

    def __str__(self):
        to_str = "[Square] "
        to_str += str(self.__width) + '/' + str(self.__height)
        return to_str
