#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    matrix_comp = [[col for col in range(3)] for row in range (3)]
    for list in matrix_comp:
        for num in list:
            print("{:d}".format(num), end=" ")
        print("{}".format("\n"), end="")
