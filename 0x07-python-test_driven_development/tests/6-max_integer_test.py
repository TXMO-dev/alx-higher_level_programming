#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([1, 5, 3, 2, 4]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1, -5, -3, -2, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4, 5]), 5)
        self.assertEqual(max_integer([-5, -4, 0, -2, -1]), 0)
        self.assertEqual(max_integer([-1, 0, -3, 2, -4]), 2)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([1, 2, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 4, 4, 4, 4]), 4)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1, 2, 1000000, 100000, 10000000]), 10000000)
        self.assertEqual(max_integer([-1000000, -2000000, -500000, -10000000]), -500000)
        self.assertEqual(max_integer([-1000000000, 0, 1000000000]), 1000000000)

if __name__ == '__main__':
    unittest.main()

