#!/usr/bin/python3
"""Test module"""
import unittest
import io
import sys
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_square(self):
        self.assertEqual(5, Square(1, 2, 3, 5).id)
    def test_square_one_arg(self):
        sq = Square(1)
        sq1 = Square(2)
        self.assertEqual(sq.id, sq1.id - 1)

    # size test cases
    def test_get_size(self):
        sq = Square(1, 2, 3, 1)
        self.assertEqual(1, sq.size)
    def test_set_size(self):
        sq = Square(1, 2, 3, 1)
        sq.size = 5
        self.assertEqual(5, sq.size)
    def test_size_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("hello")
    def test_size_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)
    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)
    def test_size_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 2, "b": 5})
    def test_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])
    def test_size_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 5, 7})
    def test_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3))
    def test_size_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))
    def test_size_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))
    def test_size_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
    def test_size_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    # x test cases
    def test_get_x(self):
        sq = Square(1, 2, 3, 1)
        self.assertEqual(2, sq.x)
    def test_set_x(self):
        sq = Square(1, 2, 3, 1)
        sq.x = 20
        self.assertEqual(20, sq.x)
    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "hi")
    def test_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)
    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 6.7)
    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 2, "b": 5})
    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])
    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 5, 7})
    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))
    def test_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'))
    def test_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'))
    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1)

    # y test cases
    def test_get_y(self):
        sq = Square(1, 2, 3, 1)
        self.assertEqual(3, sq.y)
    def test_set_y(self):
        sq = Square(1, 2, 3, 1)
        sq.y = 15
        self.assertEqual(15, sq.y)
    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "Bob")
    def test_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None)
    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 7.7)
    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {"a": 3, "b": 4})
    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, [4, 5, 6])
    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {7, 8, 9})
    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, (3, 2, 1))
    def test_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, float('nan'))
    def test_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, float('inf'))
    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -5)

class TestSquareArea(unittest.TestCase):
    def test_area(self):
        sq = Square(5, 0, 0, 1)
        self.assertEqual(25, sq.area())

    def test_area_lg_number(self):
        sq = Square(111111111111, 0, 0, 1)
        self.assertEqual(12345679012320987654321, sq.area())

    def test_atea_one_arg(self):
        sq = Square(1, 2, 3, 5)
        with self.assertRaises(TypeError):
            sq.area(1)

class TestSquareStr(unittest.TestCase):
    def test_str_sq(self):
        sq = Square(1, 2, 3, 5)
        st = f"[Square] ({sq.id}) 2/3 - 1"
        self.assertEqual(st, sq.__str__())

    def test_str_one_arg(self):
        sq = Square(1, 2, 3, 5)
        with self.assertRaises(TypeError):
            sq.__str__(1)

class TestSquareToDict(unittest.TestCase):
    def test_to_dictionary(self):
        sq = Square(1, 2, 3, 5)
        sq_dict = {'id': 5, 'x': 2, 'y': 3, 'size': 1}
        self.assertEqual(sq_dict, sq.to_dictionary())

    def test_to_dictionary_one_arg(self):
        sq = Square(1, 2, 3, 5)
        with self.assertRaises(TypeError):
            sq.to_dictionary(1)

class TestSquareUpdate(unittest.TestCase):
    def test_update_zero_arg(self):
        sq = Square(1, 2, 3, 5)
        sq.update()
        self.assertEqual("[Square] (5) 2/3 - 1", str(sq))

    def test_update_one_arg(self):
        sq = Square(1, 2, 3, 5)
        sq.update(89)
        self.assertEqual("[Square] (89) 2/3 - 1", str(sq))
 
    def test_update_two_arg(self):
        sq = Square(1, 2, 3, 5)
        sq.update(89, 10)
        self.assertEqual("[Square] (89) 2/3 - 10", str(sq))

    def test_update_three_arg(self):
        sq = Square(1, 2, 3, 5)
        sq.update(89, 10, 20)
        self.assertEqual("[Square] (89) 20/3 - 10", str(sq))

    def test_update_four_arg(self):
        sq = Square(1, 2, 3, 5)
        sq.update(89, 10, 20, 30)
        self.assertEqual("[Square] (89) 20/30 - 10", str(sq))

    def test_update_kwarg_one(self):
        sq = Square(1, 2, 3, 5)
        sq.update(id=89)
        self.assertEqual("[Square] (89) 2/3 - 1", str(sq))

    def test_update_kwarg_two(self):
        sq = Square(1, 2, 3, 5)
        sq.update(id=89, size=10)
        self.assertEqual("[Square] (89) 2/3 - 10", str(sq))

    def test_update_kwarg_three(self):
        sq = Square(1, 2, 3, 5)
        sq.update(id=89, size=10, x=20)
        self.assertEqual("[Square] (89) 20/3 - 10", str(sq))

    def test_update_kwarg_four(self):
        sq = Square(1, 2, 3, 5)
        sq.update(id=89, x=20, size=10, y=30)
        self.assertEqual("[Square] (89) 20/30 - 10", str(sq))

if __name__ == '__main__':
    unittest.main()