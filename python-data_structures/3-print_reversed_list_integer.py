#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
    new_list = list(my_list)
    new_list.reverse()
    for elements in new_list:
        print("{:d}".format(elements))
