#!/usr/bin/python3
""" 0-add_integer module

This module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """ Adds two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        The return value. a + b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
