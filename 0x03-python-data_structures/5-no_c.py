#!/usr/bin/python3


def no_c(string):
    """Removes all characters c and C from a string.

    Args:
        string: string to remove c and C characters.

    Returns:
        The return value. The new string
    """

    new_str = ''

    for character in string:
        if character not in 'cC':
            new_str += character

    return (new_str)


if __name__ == "__main__":
    no_c(string)
