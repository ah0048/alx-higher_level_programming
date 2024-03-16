#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        if not row:
            print("$")
        for i in range(len(row)):
            print("{:d}".format(row[i]), end="")
            if i == (len(row) - 1):
                print("$")
            else:
                print(end=" ")
