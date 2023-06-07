#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = [row[:] for row in matrix]
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[i])):
                new_matrix[i][j] = new_matrix[i][j] * new_matrix[i][j]
        return new_matrix
