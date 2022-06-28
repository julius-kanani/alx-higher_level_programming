#!/usr/bin/python3
""" This is the "3-say_my_name" module

The 3-say_my_name module supplies one function, say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """ Prints my name is <first_name> <last_name>

    Args:
        first_name (str): The first name.
        last_name (str): The second optional last_name.

    Returns:
        None.
    """

    if type(first_name) is str and type(last_name) is str:
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        if type(first_name) is not str:
            raise TypeError("first_name must be a string")
        if type(last_name) is not str:
            raise TypeError("last_name must be a string")
