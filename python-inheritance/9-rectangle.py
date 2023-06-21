#!/usr/bin/python3
'''Module for a func'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''subclass'''
    def __init__(self, width, height):
        '''initialisation'''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        to_str = "[Rectangle] "
        to_str += str(self.__width) + '/' + str(self.__height)
        return to_str
