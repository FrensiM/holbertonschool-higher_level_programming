#!/usr/bin/python3
""" Integer addition module """


def add_integer(a, b=98):
    """ Returns addition of a and b

    raises TypeError if a or b are not integers or floats
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    num1 = int(a)
    num2 = int(b)
    return num1 + num2