#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary

    Args:
        a_dictionary: The dictionary to be used.
        key: value to be deleted with this key.

    Returns:
        The return value. A modified dictionary
    """

    if isinstance(key, str):
        if key in a_dictionary.keys():
            del a_dictionary[key]

    return (a_dictionary)


if __name__ == "__main__":
    simple_delete(a_dictionary, key)
