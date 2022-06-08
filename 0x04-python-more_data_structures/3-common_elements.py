#!/usr/bin/python3


def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        The return value. A set of common elements in the two sets.
    """
    common_set = set()

    if (len(set_1) > 0) and (len(set_2) > 0):
        for element in set_1:
            if element in set_2:
                common_set.add(element)

    return (common_set)


if __name__ == "__main__":
    common_elements(set_1, set_2)
