#!/usr/bin/python3
"""Defines a function that rotates a 2D-matrix n x n"""


def rotate_2d_matrix(matrix):
    rotate_matrix = [[matrix[j][i] for j in
                      range(len(matrix))][::-1] for i in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        matrix[i] = rotate_matrix[i]
