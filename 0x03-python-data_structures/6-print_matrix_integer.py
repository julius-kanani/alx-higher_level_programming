#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
        matrix: The matrix to be printed.

    Returns:
        The return value. Nothing
    """

    if matrix:
        for row in matrix:
            row_len = len(row)

            for index, column in enumerate(row):
                print("{:d}{}".format(
                            column,
                            " " if (index + 1) < row_len else ""
                            ), end='')
            print()


if __name__ == "__main__":
    print_matrix_integer(matrix)
