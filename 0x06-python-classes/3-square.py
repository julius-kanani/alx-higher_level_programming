#!/usr/bin/python3
""" Defines a class square. """


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): Size of a square.
    """

    def __init__(self, size=0):
        """ Initializes a square with its size

        Args:
            size: size of square.

        Returns:
            The return value. None.
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Returns the current square area

        Args:
            None

        Returns:
            The return value. Current square area.
        """

        return (self.__size * self.__size)
