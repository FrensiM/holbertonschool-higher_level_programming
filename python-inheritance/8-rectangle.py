#!/usr/bin/python3
'''Module for a func'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''subclass'''
    def __init__(self, width, height):
        '''initialisation'''
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        self.__height = height
