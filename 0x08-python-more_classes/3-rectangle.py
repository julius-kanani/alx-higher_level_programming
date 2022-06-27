#!/usr/bin/python3
""" Module 0-rectangle

This module contains the Rectangle class.
"""


class Rectangle:
    """ Defines a Rectangle

    Attributes:
        __width (int): The width size of the rectangle.
        __height (int): The height of the rectangle.

    """

    def __init__(self, width=0, height=0):
        """ Initializes the Rectangle

        Args:
            width (int): The width size of a given rectangle.
            height (int): The height size of a given rectangle.

        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """ Returns the width of a given rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width value of a given rectangle

        Args:
            value (int): The value to set as width.

        Returns:
            None.
        """
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ Returns the height of a given rectangle. """

        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height value of a given rectangle

        Args:
            value (int): The value to set as height.

        Returns:
            None.
        """

        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ Returns the rectangle area. """

        return self.__width * self.__height

    def perimeter(self):
        """ Returns the rectangle perimeter. """

        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation of the rectangle using #. """

        string = ""
        w_size = self.__width
        h_size = self.__height
        if (w_size == 0) or (h_size == 0):
            return string
        else:
            for height in range(h_size):
                for width in range(w_size):
                    string += "#"
                    if (width + 1) == (w_size) and (height + 1) != (h_size):
                        string += "\n"

            return string
