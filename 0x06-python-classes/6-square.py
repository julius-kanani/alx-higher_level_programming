#!/usr/bin/python3
""" Defines a class square. """


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): Size of a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a square with its size

        Args:
            size (int): size of square.
            position (tuple): position of the square in 2D space.

        Returns:
            The return value. None.
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ A get method for the position private instance variable.

        Args:
            None.

        Returns:
            Current __position tuple value
        """

        return (self.__position)

    @position.setter
    def position(self, value):
        """ Sets position attribute

        Args:
            value (int): The value to set to position

        Returns:
            Nothing.
        """

        error_msg = "position must be a tuple of 2 positive integers"

        if (len(value) == 2) and (isinstance(value, tuple)):
            self.__position = value
        else:
            raise TypeError(error_msg)

    def area(self):
        """ Returns the current square area

        Args:
            None

        Returns:
            The return value. Current square area.
        """

        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #

        Args:
            None.

        Returns
            The return value. Nothing.
        """

        if self.__size == 0:
            print()
            return
        for pos_2 in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for pos in range(self.__position[0])]), end="")
            print("".join(["#" for integer in range(self.__size)]))
