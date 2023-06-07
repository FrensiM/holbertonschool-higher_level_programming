#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in sorted(set(my_list)):
        sum += i
    return sum
