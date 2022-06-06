#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position

    Args:
        my_list: list to replace an element
        idx: position to replace an existing element
        element: the element to replace an existing element

    Returns:
        The return value. if idx is -ve or out of range, return original list
        if idx is within range, add the element, return the new list
    """

    list_len = len(my_list)

    if (idx >= 0) and (idx < list_len):
        for index in range(list_len):
            if index == idx:
                my_list[index] = element
                return (my_list)

    return (my_list)


if __name__ == "__main__":
    replace_in_list(my_list, idx, element)
