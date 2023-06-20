#!/usr/bin/python3
'''Module for a func'''


class MyList(list):
    '''print a sorted list'''
    def print_sorted(self):
        list = self.copy()
        list.sort()
        print(list)
        return list
