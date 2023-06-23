#!/usr/bin/python3
'''Module of pascal triangle'''


def pascal_triangle(n):
    ''' Function that prints pascal triangle based on n'''
    tmp = [1, 1]
    matrix = []
    if n >= 1:
        matrix.append([1])
        n -= 1
    if n >= 1:
        matrix.append(tmp)
        n -= 1
    for i in range(n):
        ls = []
        for j in range(len(tmp) - 1):
            if j == 0:
                ls.append(1)
            ls.append(tmp[j] + tmp[j + 1])
            if j + 2 == len(tmp):
                ls.append(1)
        tmp = ls.copy()
        matrix.append(ls)
    return matrix
