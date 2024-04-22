#!/usr/bin/python3
'''tests for base class'''
import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


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
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_2(self):
        '''test 2'''
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
             Rectangle(10, 2, 3, -1)

    def test_3(self):
        '''test 3'''
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_4(self):
        '''test 4'''
        captured_output = StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(4, 6)
        r1.display()
        sys.stdout = sys.__stdout__
        display_output = captured_output.getvalue()
        expected_output = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(display_output, expected_output)

    def test_5(self):
        '''test_5'''
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_6(self):
        '''test 6'''
        captured_output = StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        display_output = captured_output.getvalue()
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(display_output, expected_output)

    def test_7(self):
        '''test 7'''
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_8(self):
        '''test 8'''
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(x=1, height=2, y=3, width=4, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_9(self):
        '''test 9'''
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        self.assertEqual(type(r1_dictionary), dict)

if __name__ == "__main__":
    unittest.main()