#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None

    max_element_length = len(str(max(max(matrix, key=max))))
    row_format = "{:>" + str(max_element_length) + "}"

    for row in matrix:
        for element in row:
            print(row_format.format(element), end=" ")
        print()
