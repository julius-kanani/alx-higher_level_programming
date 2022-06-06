#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order

    Args:
        my_list: list of integers, to print in reverse

    Returns:
        The return value. Nothing
    """

    for integer in my_list[::-1]:
        print("{:d}".format(integer))


if __name__ == "__main__":
    print_reversed_list_integer(my_list)
