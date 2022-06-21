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
            size (int): size of square.

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

    @property
    def size(self):
        """ A get method for private instance variable __size.

        Args:
            None.

        Returns
            The return value. current __size value.
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """ A set method for private instance variable __size

        Args:
            Value (int): The value to set __size to.

        Returns:
            The return value. Nothing.
        """

        if isinstance(value, int):
            if value >= 0:
                self.__size = value
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
