#!/usr/bin/python3
""" Integer addition module """


def matrix_divided(matrix, div):
    '''take a matric and fivides every int or float'''
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_len = len(matrix[0])
    new_matrix = []
    for row in matrix:
        new_row = []
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in [int, float]:
                raise_err()
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix


def raise_err():
    a = 'matrix must be a matrix (list of lists) of integers/floats'
    raise TypeError(a)
