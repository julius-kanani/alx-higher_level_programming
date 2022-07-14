#!/usr/bin/python3
""" The test_rectangle module

This module supplies all the test case scenarios for the Rectangle class.
"""


from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """ Test cases for the Rectangle class. """

    def test_obj_rectangle_no_args(self):
        """ Test for when no arguments provided for the Rectangle class. """

        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_obj_rectangle_excess_args(self):
        """ Excess arguments provided. """

        with self.assertRaises(TypeError):
            r2 = Rectangle(1, 1, 1, 1, 1, 1, 1)

    def test_obj_rectangle_has_id(self):
        """ Checks if Rectangle inherits Base class. """

        r3 = Rectangle(3, 5)
        self.assertEqual(r3.id, 2)

    def test_obj_rectangle_correct_input(self):
        """ Tests for incorrect arguments. """

        with self.assertRaises(TypeError):
            r4 = Rectangle("Hi", "There")
