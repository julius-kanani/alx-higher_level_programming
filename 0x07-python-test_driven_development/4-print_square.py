#!/usr/bin/python3
""" This is the "4-print_square" module

This module supplies one function, print_square(size).
"""


def print_square(size):
    """ Prints a square with the character #

    Args:
        size (int): The size of the square.

    Returns:
        None.
    """

    if type(size) is int:
        if size >= 0:
            for length in range(size):
                for width in range(size):
                    print("#", end='')
                print()
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
