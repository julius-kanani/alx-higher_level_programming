#!/usr/bin/python3


def max_integer(my_list=[]):
    """Finds the biggest integer of a list

    Args:
        my_list: List to look for its biggest integer.

    Returns:
        The return value. biggest integer
        if list is empty, return None
    """

    if len(my_list) > 0:
        max_int = my_list[0]
        for integer in my_list:
            if integer > max_int:
                max_int = integer

        return (max_int)
    else:
        return (None)


if __name__ == "__main__":
    max_integer(my_list)
