#!/usr/bin/python3
'''tests for base class'''
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
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
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_2(self):
        '''test 2'''
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, {"id": 1, "width": 10,
                                      "height": 7, "x": 2, "y": 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(json_dictionary, '[{"id": 1, "width": 10, '
                         '"height": 7, "x": 2, "y": 8}]')
        self.assertEqual(type(json_dictionary), str)

    def test_3(self):
        '''test 3'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(),
                             '[{"id": 1, "width": 10, '
                             '"height": 7, "x": 2, "y": 8}, '
                             '{"id": 2, "width": 2, '
                             '"height": 4, "x": 0, "y": 0}]')

    def test_4(self):
        '''test 4'''
        list_input = [
                        {'id': 89, 'width': 10, 'height': 4},
                        {'id': 7, 'width': 1, 'height': 7}
                    ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual("[{}] {}".format(type(list_input), list_input),
                         "[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]")
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(json_list_input, '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]')
        self.assertEqual("[{}] {}".format(type(list_output), list_output),
                         "[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]")

    def test_5(self):
        '''test 5'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1 == r2, False)

    def test_6(self):
        '''test 6'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_input[0]), "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(str(list_rectangles_input[1]), "[Rectangle] (2) 0/0 - 2/4")
        self.assertEqual(str(list_rectangles_output[0]), "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(str(list_rectangles_output[1]), "[Rectangle] (2) 0/0 - 2/4")
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_input[0]), "[Square] (5) 0/0 - 5")
        self.assertEqual(str(list_squares_input[1]), "[Square] (6) 9/1 - 7")
        self.assertEqual(str(list_squares_output[0]), "[Square] (5) 0/0 - 5")
        self.assertEqual(str(list_squares_output[1]), "[Square] (6) 9/1 - 7")

if __name__ == "__main__":
    unittest.main()