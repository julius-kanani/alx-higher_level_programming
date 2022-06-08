#!/usr/bin/python3


def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        The return value. A set of common elements in the two sets.
    """

    return (set_1 & set_2)


if __name__ == "__main__":
    common_elements(set_1, set_2)
