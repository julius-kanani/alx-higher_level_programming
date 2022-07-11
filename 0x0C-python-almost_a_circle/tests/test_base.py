#!/usr/bin/python3
""" The test_base module

This module contains test cases scenarios for the base model.
"""

from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """ Test cases for the Base model. """

    def test_no_id(self):
        """ Tests for id not given. """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_given(self):
        """ Tests id given. """
        b2 = Base(5)
        self.assertEqual(b2.id, 5)

    def test_type_id(self):
        """ Tests Type for id. """
        
        with self.assertRaises(TypeError):
            b2 = Base("Incorrect Type")

    def test_base_no_args(self):
        """ Tests for more than one argument provided. """

        with self.assertRaises(TypeError):
            b3 = Base(1, 1)
