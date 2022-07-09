#!/usr/bin/python3
""" The base module
This module supplies the Base Class.
"""

import json


class Base:
    """ Defines the Base class

    Attributes:
        __nb_objects (int): private class attribute, records no of instances

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the Base class

        Args:
            id (int): Unique identifier for class

        Returns:
            None.
        """
        self.id = id

    @property
    def id(self):
        """ Returns the id value """

        return self.__id

    @id.setter
    def id(self, id=None):
        """ Sets id value """

        if id is not None:
            self.__id = id
        else:
            type(self).__nb_objects += 1
            self.__id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the json string representation of list_dictionaries. """

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
