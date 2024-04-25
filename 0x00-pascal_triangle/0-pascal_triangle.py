#!/usr/bin/python3


def pascal_triangle(n):
    """
        returns a list of lists of integers representing 
        the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    n0 = [1]
    n1 = [1, 1]

    if n == 1:
        return [n0]

    if n == 2:
        return [n0, n1]

    if n > 1:
        triangle = [n0, n1]
        for i in range(3, n + 1):
            row = []
            intArr = triangle[-1]   

            for index in range(len(intArr) -1):
                row.append(intArr[index]+intArr[index + 1])

            row.insert(0, 1)
            row.append(1)
            triangle.insert(i, row)

        return triangle    