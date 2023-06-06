#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ls in matrix:
        for i in range(len(ls)):
            if i == len(ls) - 1:
                print("{:d}".format(ls[i]), end="")
            else:
                print("{:d}".format(ls[i]), end=" ")
        print()