#!usr/bin/python3
""" This is the "5-text_indentation" module

This module supplies one function, text_indentation.
"""


def text_indentation(text):
    """ Prints a text with 2 new lines after each of these characters [. ? :]

    Args:
        text (str): The text to be used.

    Returns:
        None.
    """
    look_for = [".", "?", ":"]

    if type(text) is str:
        flag = 0
        for char in text:
            if flag == 0:
                if char == " ":
                    continue
                else:
                    flag = 1
            if flag == 1:
                if char in look_for:
                    print(char)
                    print()
                    flag = 0
                else:
                    print(char, end='')
    else:
        raise TypeError("text must be a string")
