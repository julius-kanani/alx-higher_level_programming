#!/usr/bin/python3
from calculator_1 import add, mul, div, sub


def calculator():
    """A simple calculator that can add, sub, mul, div

    Args:
       No arguments

    Returns:
       The return value. Returns Nothing
    """

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    calculator()
