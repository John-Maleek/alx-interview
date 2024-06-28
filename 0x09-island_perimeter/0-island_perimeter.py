#!/usr/bin/python3
"""Module defines a peremeter determining
    function
"""


def island_perimeter(grid):
    """Returns the perimeter value based on grid input"""
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                continue
            else:
                if grid[i][j-1] == 0:
                    perimeter += 1
                if grid[i][j+1] == 0:
                    perimeter += 1
                if grid[i-1][j] == 0:
                    perimeter += 1
                if grid[i+1][j] == 0:
                    perimeter += 1
    return perimeter
