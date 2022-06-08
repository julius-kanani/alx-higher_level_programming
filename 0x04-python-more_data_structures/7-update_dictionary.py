#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/ value in a dictionary.

    Args:
        a_dictionary: The dictionary to be used.
        key: Dictionary key to be used to retrieve value.
        value: value to be inserted by a specific key.

    Returns:
        The return value. A new dictionary.
    """

    if isinstance(key, str):
        a_dictionary.update({key: value})

    return (a_dictionary)
