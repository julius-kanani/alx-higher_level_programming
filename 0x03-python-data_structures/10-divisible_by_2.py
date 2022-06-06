#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list

    Args:
        my_list: list to look for multiples of two.

    Returns:
        The return value. A true or False list if int is a multiple of 2
    """

    if len(my_list) > 0:
        new_list = []
        for integer in my_list:
            if (integer % 2 == 0):
                new_list.append(True)
            else:
                new_list.append(False)

        return (new_list)
    return (None)


if __name__ == "__main__":
    divisible_by_2(my_list)
