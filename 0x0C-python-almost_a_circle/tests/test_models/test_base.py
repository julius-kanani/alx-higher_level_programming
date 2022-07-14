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

    def test_empty_to_json_string(self):
        """ Test for passing empty list. """

        json_string = Base.to_json_string([])
        self.assertTrue(type(json_string) is str)
        self.assertEqual(json_string, "[]")

    def test_None_to_json_String(self):
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """Tests regular from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_fjs_empty(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual(Base.from_json_string(""), [])

    def test_fjs_None(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(None))
