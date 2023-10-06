#!/usr/bin/python3
"""Unittest class to test files"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """Tescase to test max_integer function"""

    def test_empty(self):
        """Function to test for None input to max_integer"""
        self.assertIsNone(max_integer([]))

    def test_Max(self):
        """Function to test for Max number in a list"""
        self.assertEqual(max_integer([1, 2, 10, 3]), 10)

    def test_NotMax(self):
        """Function to test if not max number"""
        self.assertNotEqual(max_integer([1, 2, 10, 3]), 1)

    def test_TypeErr(self):
        """Function to test TypeErrors"""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 2, 4,])

    def test_None(self):
        """Function to test None TypeErrors"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_negativeInt(self):
        """Function to test for Negative"""
        self.assertEqual(max_integer([-1, -3, -4, -5]), -1)

    def test_OneElement(self):
        """Function to test for one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_ElementMiddle(self):
        """Function to test for element in middle"""
        self.assertEqual(max_integer([1, 2, 60, 4, 5]), 60)

    def test_OneNagative(self):
        """Function to test for only one negative number"""
        self.assertEqual(max_integer([-1, 10, 4, 5]), 10)

    def test_MaxAtBeginning(self):
        """Function to test for the max at the beginning"""
        self.assertEqual(max_integer([100, 1, 2, 4]), 100)

    def test_MaxAtEnd(self):
        """function to test for the max at the end of a list"""
        self.assertEqual(max_integer([1, 2, 3, 4, 100]), 100)


if __name__ == "__main__":
    unittest.main()
