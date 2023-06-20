#!/usr/bin/python3
'''Module for a func'''


def inherits_from(obj, a_class):
    '''fun that check if a obj is inherits'''
    return isinstance(obj, a_class) or any(issubclass(type(obj), cls) for cls in a_class.__subclasses__())
