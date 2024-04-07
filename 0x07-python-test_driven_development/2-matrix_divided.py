#!/usr/bin/python3
'''module for matrix division'''


def matrix_divided(matrix, div):
    '''method for matrix division'''

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = len(matrix[0])
    new_matrix = []
    for rows in matrix:
        if not isinstance(rows, list) or len(rows) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(rows) != size:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(elements, (int, float)) for elements in rows):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_row = []
        for elements in rows:
            new_row.append(round(elements / div, 2))
        new_matrix.append(new_row)
    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
