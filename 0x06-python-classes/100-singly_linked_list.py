#!/usr/bin/python3
""" A class Node that defines a node of a singly linked List """


class Node:
    """ Node of a singly linked list

    Attributes:
        __data (int): Data stored by a node.
        __next_node (Node): Next node in the singly linked list.

    """

    def __init__(self, data, next_node=None):
        """ Initializes a Node, with data and the next node

        Args:
            data (int): Data stored by a node.
            next_node (Node): Next node.

        Returns:
            None
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Gets the value of data of a Node

        Args:
            None.

        Returns:
            The value of data of a node.
        """

        return (self.__data)

    @data.setter
    def data(self, value):
        """ Sets the value of data of a Node

        Args:
            value (int): The integer to assign to data.

        Returns:
            None.
        """

        if type(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ Gets the next node in Linked linked list from the current node

        Args:
            None.

        Returns:
            The next node of a single linked list.
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ Sets the value of the next node of a single linked list in a node

        Args:
            value (Node): The next_node to set to in the current node.

        Returns:
            None.
        """

        if type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ Creates a Singly linked list

    Attributes:
        __head (Node): The head of singly linked list.
    """

    def __init__(self):
        """ Initializes a Singly Linked List

        Args:
            None.

        Returns:
            None.
        """

        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new Node into the correct sorted position in the list
            (increasing order)

        Args:
            value (int): The integer to insert into a new node.

        Returns:
            None.
        """
        new_node = None
        if type(value) is int:
            new_node = Node(value)
        else:
            raise TypeError("data must be an integer")

        current = self.__head

        if self.__head is None:
            self.__head = new_node
        else:
            if (new_node.data >= current.data):
                while (new_node.data >= current.data) and current.next_node:
                    prev = current
                    current = current.next_node
                if (new_node.data < current.data):
                    prev.next_node = new_node
                    new_node.next_node = current
                else:
                    current.next_node = new_node
            else:
                new_node.next_node = current
                self.__head = new_node

    def __str__(self):
        """ String representation of Singly Linked List

        Args:
            None.

        Returns:
            Formatted string representation of a singly linked list.
        """

        string = ""

        current = self.__head
        while (current is not None):
            string += str(current.data)
            if current.next_node is not None:
                string += "\n"
            current = current.next_node

        return (string)
