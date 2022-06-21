#!/usr/bin/python3
""" Defines a class square. """


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): Size of a square.
    """

    def __init__(self, size):
        """ Initializes a square with its size

        Args:
            size: size of square.

        Returns:
            The return value. None.
        """
        self.__size = size
