#!/usr/bin/python3
'''Module for a func'''


def is_kind_of_class(obj, a_class):
    '''check if obj in same class'''
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
