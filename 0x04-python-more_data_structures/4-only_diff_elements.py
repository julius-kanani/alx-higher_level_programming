#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        The return value. A set of all elements present only in one set.
    """

    only_diff_elements_set = set()

    if (len(set_1) > 0) and (len(set_2) > 0):
        only_diff_elements_set = set_1 ^ set_2

    return (only_diff_elements_set)


if __name__ == "__main__":
    only_diff_elements(set_1, set_2)
