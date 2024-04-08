#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax(unittest.TestCase):
    """Unittest for max_integer([..])"""

    def test_0(self):
        """Unittest for max_integer([..])"""
        max = max_integer([1, 2, 3, 4])
        self.assertEqual(max, 4)
    

    def test_1(self):
        """Unittest for max_integer([..])"""
        max = max_integer([1, 3, 4, 2])
        self.assertEqual(max, 4)
    
    def test_2(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([1, 3, 4, "hi"])


if __name__ == "__main__":
    unittest.main()
