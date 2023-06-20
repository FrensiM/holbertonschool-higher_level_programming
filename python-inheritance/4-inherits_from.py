#!/usr/bin/python3
'''Module for a func'''


def inherits_from(obj, a_class):
    '''fun that check if a obj is inherits'''
    if isinstance(obj, a_class):
        if obj.__class__ is a_class:
            return False
        return True
    return False
