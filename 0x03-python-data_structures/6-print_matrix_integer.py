#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        if not row:
            print("$")
        for element in row:
            print("{:d}".format(element), end="")
            if row.index(element) == (len(row) - 1):
                print("$")
            else:
                print(end=" ")
