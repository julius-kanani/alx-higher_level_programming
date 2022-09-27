#!/usr/bin/python3
""" 6-peak module. Contains the find_peak function. """


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): The list of unsorted integers.
    """
    peak_list = []
    lst_size = len(list_of_integers)

    if lst_size == 0:
        return None
    elif lst_size < 3:
        return max(list_of_integers)
    elif list_of_integers[0] > list_of_integers[1]:
        return abs(list_of_integers[0])
    elif list_of_integers[-1] > list_of_integers[-2]:
        return abs(list_of_integers[-1])

    for i in range(1, lst_size):
        if list_of_integers[i] >= list_of_integers[i - 1] \
           and list_of_integers[i] >= list_of_integers[i + 1]:
            return abs(list_of_integers[i])
