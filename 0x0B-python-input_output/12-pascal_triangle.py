#!/usr/bin/python3
'''module for pascal'''


def pascal_triangle(n):
    '''returns a list of lists of integers representing the Pascal’s triangle of n'''
    if n <= 0:
        return []
    matrix = []
    for i in range(n):
        row = []
        if i == 0:
            row.append(1)
        else:
            for j in range(len(matrix[i - 1]) + 1):
                if j == 0:
                    row.append(matrix[i - 1][j])
                elif j == len(matrix[i - 1]):
                    row.append(matrix[i - 1][j - 1])
                else:
                    row.append(matrix[i - 1][j] + matrix[i - 1][j - 1])
        matrix.append(row)
    return matrix
