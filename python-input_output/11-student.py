#!/usr/bin/python3
"""Student class Module"""


class Student:
    """Class named student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        d = {}
        if attrs is None:
            for attr, value in self.__dict__.items():
                d[attr] = value
        else:
            for string in attrs:
                if type(string) is str:
                    if string in self.__dict__.keys():
                        d[string] = self.__dict__[string]
        return d

    def reload_from_json(self, json):
        for attr in json.keys():
            if attr in self.__dict__.keys():
                self.__dict__[attr] = json[attr]
