#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5 Dec 2024

@author: Ghyath Ibrahim
"""

import unittest

from ..add import add

class TestMystery1(unittest.TestCase):
    """ test the add function """
    
    def test_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_negative_numbers(self):
        self.assertEqual(add(-3, -7), -10)

    def test_mixed_numbers(self):
        self.assertEqual(add(10, -5), 5)

    def test_with_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)

    def test_non_numeric_first_argument(self):
        with self.assertRaises(ValueError):
            add("a", 5)

    def test_non_numeric_second_argument(self):
        with self.assertRaises(ValueError):
            add(5, "b")

    def test_both_arguments_non_numeric(self):
        with self.assertRaises(ValueError):
            add("a", "b")

    def test_none_as_argument(self):
        with self.assertRaises(ValueError):
            add(None, 5)
        with self.assertRaises(ValueError):
            add(5, None)
