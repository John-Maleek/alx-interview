#!/usr/bin/python3
"""
Module defies a method that calculates the fewest
number of operations needed to result in exactly
n H characters in a given file
"""


def minOperations(n):
    """
    returns the fewest number of operation needed
    to result in exactly n H characters
    """
    x = 0
    y = 2
    while n > 1:
        while n % y == 0:
            x += y
            n = n / y
        y += 1
    return x
