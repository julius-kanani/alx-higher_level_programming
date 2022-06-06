#!/usr/bin/python3


def element_at(my_list, idx):
    """Retrieves an element from a list

    Args:
        my_list: list to retrieve an element from.
        idx: position to retrieve an element in a list.

    Returns:
        The return value. None if idx is negative, and if idx is out of range
    """

    list_len = len(my_list)

    if (idx >= 0) and (idx < list_len):
        for index, element in enumerate(my_list):
            if index == idx:
                return (element)

    return (None)


if __name__ == "__main__":
    element_at(my_list, idx)
