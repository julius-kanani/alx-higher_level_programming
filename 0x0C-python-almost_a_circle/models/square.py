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

    @property
    def size(self):
        """ Returns the value of size. """

        return self.width

    @size.setter
    def size(self, value):
        """ Sets the size of the Square instance. """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the class Square by assigning attributes. """

        if len(args) > 0:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                if kwargs["id"] is None:
                    super().__init__(self.size, self.x, self.y)
                else:
                    self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """ A string representation of the Square class. """

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)
