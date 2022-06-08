#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys

    Args:
        a_dictionary: The dictionary to print.

    Returns:
        The return value. a sorted dictionary.
    """

    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary.get(key)))


if __name__ == "__main__":
    printed_sorted_dictionary(a_dictionary)
