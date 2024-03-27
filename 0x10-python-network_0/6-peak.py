#!/usr/bin/python3
""" 6-peak module. Contains the find_peak function. """


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): The list of unsorted integers.
    """

    if not list_of_integers:
        return None
    # Binary search for a peak
    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
