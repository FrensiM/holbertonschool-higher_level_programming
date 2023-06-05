#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = list(my_list)
    new_list.reverse()
    for element in new_list:
        print("{:d}".format(element))
