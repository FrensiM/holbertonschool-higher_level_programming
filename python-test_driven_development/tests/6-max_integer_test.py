#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 3, 6, 8]), 8)
        self.assertAlmostEqual(max_integer([1, 5, 10, 7]), 10)
        self.assertAlmostEqual(max_integer([13, 5, 7, 8]), 13)
        self.assertAlmostEqual(max_integer([1, 5, -4, -2]), 5)
        self.assertAlmostEqual(max_integer([-6, -15, -1, -8]), -1)
        self.assertAlmostEqual(max_integer([7]), 7)
        self.assertAlmostEqual(max_integer(), None)
