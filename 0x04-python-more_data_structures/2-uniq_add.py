#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer).

    Args:
        my_list: list to add its integers.

    Returns:
        The return value. Sum of all unique integers.
    """
    int_sum = 0

    if (len(my_list) > 0):
        add_memory = set()
        for integer in my_list:
            if integer not in add_memory:
                int_sum += integer
                add_memory.add(integer)
        return (int_sum)

    return (int_sum)


if __name__ == "__main__":
    uniq_add(my_list)
