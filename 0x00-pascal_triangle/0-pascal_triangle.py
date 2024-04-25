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
        return []

    if n > 1:
        triangle = [[1]]
        for i in range(1, n):
            row = []
            intArr = triangle[-1]   

            for index in range(len(intArr) -1):
                row.append(intArr[index]+intArr[index + 1])

            row.insert(0, 1)
            row.append(1)
            triangle.insert(i, row)

        return triangle