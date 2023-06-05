#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num1 in matrix:
        for num2 in range(len(num1)):
            if num2 == len(num1) - 1:
                print("{:d}".format(num1[num2]), end="")
            else:
                print("{:d}".format(num1[num2]), end="")
        print()
