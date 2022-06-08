#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    """Returns a list with all values multiplied by a number.

    Args:
        my_list: A list with values
        number: number to multiply with each value of the list

    Returns:
        The return value. A new list
    """

    new_list = my_list[:]

    if (len(my_list) > 0):
        result = map(lambda x: x * number, new_list)
        return (list(result))

    return (my_list)


if __name__ == "__main__":
    multiply_list_map(my_list, number)
