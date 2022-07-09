#!/usr/bin/python3
""" The square module

This module supplies the Square class, that inherits from the rectangle class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines the Square class.

    Class Attributes:
        None.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the Square class.

        Args:
            size (int): The size of the square.
            x (int): The x coordinate.
            y (int): The y coordinate.
            id (int): The unique identifier of the rectangle instance.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ A string representation of the Square class. """

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)
