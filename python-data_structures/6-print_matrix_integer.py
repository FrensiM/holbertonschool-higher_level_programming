#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num1 in matrix:
        for i in range(len(num1)):
            if i == len(num1) - 1:
                print("{:d}".format(num1[i]), end="")
            else:
                print("{:d}".format(num1[i]), end=" ")
        print()
