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
            if type(id) is not int:
                raise TypeError("id must be > 0")
            self.__id = id
        else:
            type(self).__nb_objects += 1
            self.__id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the json string representation of list_dictionaries.

        Args:
            list_dictionaries: Dictionary representations of instances."
        """

        if type(list_dictionaries) is not list:
            return "[]"

        if (list_dictionaries is None) or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (instance): A list of instances.

        Return:
            None.
        """

        filename = cls.__name__ + ".json"
        obj_dicts = []

        if list_objs is not None:
            for obj in list_objs:
                obj_dicts.append(cls.to_dictionary(obj))
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(obj_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation.

        Args:
            json_string (json): The json string.
        """

        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set.

        Args:
            dictionary: A dictionary of attributes of a class.
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances. """

        # file name to read from
        filename = cls.__name__ + ".json"
        # list to record instances as they are being created
        instances = []
        try:
            with open(filename, "r") as file:
                # Read from the file, a json_string
                json_string = file.read()
                # convert the json string to dictionaries
                list_dict = cls.from_json_string(json_string)

                # create the instances for every available dictionary.
                for dictionary in list_dict:
                    obj = cls.create(**dictionary)
                    instances.append(obj)

            return instances

        except FileNotFoundError as Error:
            return []
