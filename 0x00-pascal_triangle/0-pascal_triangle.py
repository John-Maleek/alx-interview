#!/usr/bin/python3
"""
Module defines a pascal's triangle function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    Returns: an empty list if n <= 0
    """
    if n <= 0:
        return [[]]

    elif n > 1:
        triangle = [[1]]
        for i in range(1, n):
            row = []
            prev_row = triangle[-1]
            row = [prev_row[index] + prev_row[index + 1]
                   for index in range(len(prev_row) - 1)]
            row.insert(0, 1)
            row.append(1)
            triangle.insert(i, row)

        return triangle
