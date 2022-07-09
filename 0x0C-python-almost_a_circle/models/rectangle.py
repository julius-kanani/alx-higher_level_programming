#!/usr/bin/python3
""" The rectangle module

Supplies the Rectangle class.
"""


from models.base import Base


class Rectangle(Base):
    """ Defines the Rectangle class
        Inherits the Base class

    Attributes:
        __width (int): The width.
        __height (int): The rectangle height.
        __x (int): The x.
        __y: (int): The y.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the Rectangle class

        Args:
            width (int): The rectangle width.
            height (int): The rectangle height.
            x (int): The x coordinate.
            y (int): The y coordinate.
            id (int): Unique identifier.

        Returns:
            None.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Returns the width of the rectangle. """

        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle. """
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ Returns the height of the rectangle. """

        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle. """

        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """ Returns the x coordinate. """

        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the x coordinate. """

        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """ Returns the y coordinate. """

        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the y coordinate. """

        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be > 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """ Returns the area value of the Rectangle instance, """

        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character #. """
        lines = self.__y
        for i in range(self.__height):
            if lines > 0:
                while lines > 0:
                    print()
                    lines -= 1
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute. """

        if len(args) > 0:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.__width = arg
                elif index == 2:
                    self.__height = arg
                elif index == 3:
                    self.__x = arg
                elif index == 4:
                    self.__y = arg
                else:
                    raise Exception("Out of Order")
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns the dictionary representation of a rectangle. """

        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """ Returns a string representation of a Rectangle instance. """

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
