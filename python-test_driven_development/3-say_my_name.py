#!/usr/bin/python3
""" Integer addition module """


def say_my_name(first_name, last_name=""):
    '''gets a name and a surname if provided and prints the full name'''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
