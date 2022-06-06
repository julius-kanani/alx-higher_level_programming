#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """Prints all integers of a list

    Args:
        my_list: The list to be printed

    Returns:
        The return value. Nothing.
    """

    for integer in my_list:
        print("{:d}".format(integer))


if __name__ == "__main__":
    print_list_integer(my_list)
