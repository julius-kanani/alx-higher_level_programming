#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character

    Args:
        sentence: The string to be used

    Returns:
        The return value. A tuple (Length of a string, its first character)
    """
    str_len = 0
    first_char = None

    if sentence:
        str_len = len(sentence)
        first_char = sentence[0]

    return (str_len, first_char)


if __name__ == "__main__":
    multiple_returns(sentence)
