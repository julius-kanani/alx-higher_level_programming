#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    Args:
        matrix: the matrix to compute the square value of all integers of
                of a matrix.

    Returns:
        The return value. a new matrix, same size as the matrix, each value
        should be the square value of the input.
    """

    new_matrix = [[column ** 2 for column in row] for row in matrix]

    return (new_matrix)


if __name__ == "__main__":
    square_matrix_simple(matrix)
