#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary: The dictionary to be used.

    Returns:
        The return value. A modified dictionary.
    """

    if (len(a_dictionary) > 0):
        new_dict = {}
        for key, value in a_dictionary.items():
            new_dict[key] = value * 2

        return (new_dict)

    return (a_dictionary)


if __name__ == "__main__":
    multiply_by_2(a_dictionary)
