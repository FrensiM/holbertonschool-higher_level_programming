#!/usr/bin/python3
"""Class to json Module"""


def class_to_json(obj):
    """Class to json func"""
    d = {}
    for attr, value in obj.__dict__.items():
        d[attr] = value
    return d
