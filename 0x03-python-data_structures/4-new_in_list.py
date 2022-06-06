#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position without modifying
    the original list.

    Args:
        my_list: List to be modified.
        idx: position to replace an element in a given list.
        element: element to replace into a given list in a specified position.

    Returns:
        The return value. if idx is -ve, or out of range, return original list
        if idx is within range, return the modified list.
    """

    new_list = []

    for index, item in enumerate(my_list):
        new_list.append(item)

    len_nl = len(new_list)

    if (idx >= 0) and (idx < len_nl):
        new_list[idx] = element
        return (new_list)

    return (my_list)


if __name__ == "__main__":
    new_in_list(my_list, idx, element)
