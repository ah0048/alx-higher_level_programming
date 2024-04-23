#!/usr/bin/python3
'''tests for base class'''
import unittest
import sys
from io import StringIO
from models.base import Base
from models.square import Square


class TestRectangle(unittest.TestCase):
    '''test cases'''

    def setUp(self):
        '''initialization before each test'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''cleans after each test'''
        pass

    def test_1(self):
        '''test 1'''
        captured_output = StringIO()
        sys.stdout = captured_output
        s1 = Square(5, 1, 3)
        self.assertEqual(str(s1), "[Square] (1) 1/3 - 5")
        self.assertEqual(s1.area(), 25)
        s1.display()
        sys.stdout = sys.__stdout__
        display_output = captured_output.getvalue()
        expected_output = "\n\n\n #####\n #####\n #####\n #####\n #####\n"
        self.assertEqual(display_output, expected_output)

    def test_2(self):
        '''test 2'''
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        with self.assertRaises(TypeError):
            s1.size = "9"
        with self.assertRaises(ValueError):
            s1.size = -9

    def test_3(self):
        '''test 3'''
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 3/1 - 7")

    def test_4(self):
        '''test 4'''
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (4) 2/3 - 1")

    def test_5(self):
        Square.save_to_file(None)
        Square.save_to_file([])
        Square.save_to_file([Square(1)])

if __name__ == "__main__":
    unittest.main()