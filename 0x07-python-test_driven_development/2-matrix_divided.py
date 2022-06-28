#!/usr/bin/python3
""" 2-matrix_divided module

This module contains the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """ Divides all the elements of a matrix.

    Args:
        matrix (int) or (floats): List lists of integers or floats.
        div (int) or (float): The divisor.

    Returns:
        A new matrix divided by div.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None:
        raise TypeError(error_msg)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    else:
        if div == 0:
            raise ZeroDivisionError("division by zero")

    each_row_is_list = all(map(lambda row: type(row) is list, matrix))
    if (type(matrix) is list) and (each_row_is_list):
        new_matrix = [[column for column in row] for row in matrix]
        if all(map(lambda row: len(row) == len(matrix[0]), matrix)):
            for row in matrix:
                if not all(map(lambda col: type(col) in [int, float], row)):
                    raise TypeError(error_msg)
            new_matrix = [
                    [round(column / div, 2) for column in row]
                    for row in matrix
                    ]
        else:
            raise TypeError("Each row of the matrix must have the same size")
    else:
        raise TypeError(error_msg)

    return new_matrix
