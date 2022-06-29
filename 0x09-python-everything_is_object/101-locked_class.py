#!/usr/bin/python3
""" Module 101-locked_class

This module supplies one class LockedClass.
"""


class LockedClass:
    """ prevents user from dynamically creating new instance attributes. """
    __slots__ = ['first_name']
