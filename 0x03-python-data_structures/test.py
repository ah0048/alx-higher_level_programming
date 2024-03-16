#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        if not row:
            print("$")
        else:
            for index, element in enumerate(row):
                print("{:d}".format(element), end="")
                if index == len(row) - 1:
                    print("$")
                else:
                    print(end=" ")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
