#!/usr/bin/python3
"""Test module"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rect(self):
        self.assertEqual(5, Rectangle(1, 2, 3, 4, 5).id)

    # width test cases
    def test_get_width(self):
        rect = Rectangle(1, 2, 3, 4, 1)
        self.assertEqual(1, rect.width)
    def test_set_width(self):
        rect = Rectangle(1, 2, 3, 4, 1)
        rect.width = 5
        self.assertEqual(5, rect.width)
    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hello", 2)
    def test_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)
    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 2)
    def test_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 2, "b": 5}, 2)
    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)
    def test_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 5, 7}, 2)
    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)
    def test_width_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)
    def test_width_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)
    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    # height test cases
    def test_get_height(self):
        rect = Rectangle(1, 2, 3, 4, 1)
        self.assertEqual(2, rect.height)
    def test_set_height(self):
        rect = Rectangle(1, 2, 3, 4, 1)
        rect.height = 10
        self.assertEqual(10, rect.height)
    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "hi")
    def test_height_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)
    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 6.7)
    def test_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 2, "b": 5})
    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])
    def test_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 5, 7})
    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))
    def test_height_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))
    def test_height_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))
    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)
    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    # x test cases
    def test_get_x(self):
        rect = Rectangle(1, 2, 3, 4, 1)
        self.assertEqual(3, rect.x)
    def test_set_x(self):
        rect = Rectangle(1, 2, 3, 4, 1)
        rect.x = 20
        self.assertEqual(20, rect.x)
    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "hi")
    def test_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)
    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 6.7)
    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 2, "b": 5})
    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3])
    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 5, 7})
    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3))
    def test_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'))
    def test_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'))
    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -1)

    # y test cases
    def test_get_y(self):
        rect = Rectangle(1, 2, 3, 4, 1)
        self.assertEqual(4, rect.y)
    def test_set_y(self):
        rect = Rectangle(1, 2, 3, 4, 1)
        rect.y = 15
        self.assertEqual(15, rect.y)
    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "Bob")
    def test_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)
    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 7.7)
    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {"a": 3, "b": 4})
    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, [4, 5, 6])
    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {7, 8, 9})
    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, (3, 2, 1))
    def test_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, float('nan'))
    def test_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, float('inf'))
    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -5)

class TestRectangleArea(unittest.TestCase):
    def test_area(self):
        rect = Rectangle(5, 10, 0, 0, 1)
        self.assertEqual(50, rect.area())

    def test_area_lg_number(self):
        rect = Rectangle(111111111111, 111111111111, 0, 0, 1)
        self.assertEqual(12345679012320987654321, rect.area())

    def test_atea_one_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.area(1)

class TestRectangleStr(unittest.TestCase):
    def test_str_rect(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        st = f"[Rectangle] ({rect.id}) 3/4 - 1/2"
        self.assertEqual(st, rect.__str__())

    def test_str_one_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.__str__(1)

class TestRectangleDisplay(unittest.TestCase):
    # Get and return text printed to stdout
    @staticmethod
    def get_stdout(rect, method):
        get_rec = io.StringIO()
        sys.stdout = get_rec
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return get_rec
    
    def test_diplay_rect(self):
        rect = Rectangle(1, 2, 0, 0, 1)
        capture = TestRectangleDisplay.get_stdout(rect, "display")
        self.assertEqual("#\n#\n", capture.getvalue())

    def test_display_rect_width_height_x(self):
        rect = Rectangle(1, 2, 3, 0, 1)
        capture = TestRectangleDisplay.get_stdout(rect, "display")
        self.assertEqual("   #\n   #\n", capture.getvalue())

    def test_display_one_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.display(1)

class TestRectangleToDict(unittest.TestCase):
    def test_to_dictionary(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect_dict = {'id': 5, 'x': 3, 'y': 4, 'width': 1, 'height': 2}
        self.assertEqual(rect_dict, rect.to_dictionary())

    def test_to_dictionary_one_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.to_dictionary(1)

class TestRectangleUpdate(unittest.TestCase):
    def test_update_zero_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update()
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(rect))

    def test_update_one_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(89)
        self.assertEqual("[Rectangle] (89) 3/4 - 1/2", str(rect))
 
    def test_update_two_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(89, 10)
        self.assertEqual("[Rectangle] (89) 3/4 - 10/2", str(rect))

    def test_update_three_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(89, 10, 20)
        self.assertEqual("[Rectangle] (89) 3/4 - 10/20", str(rect))

    def test_update_four_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(89, 10, 20, 30)
        self.assertEqual("[Rectangle] (89) 30/4 - 10/20", str(rect))

    def test_update_five_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(89, 10, 20, 30, 40)
        self.assertEqual("[Rectangle] (89) 30/40 - 10/20", str(rect))

    def test_update_kwarg_one(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=89)
        self.assertEqual("[Rectangle] (89) 3/4 - 1/2", str(rect))

    def test_update_kwarg_two(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=89, width=10)
        self.assertEqual("[Rectangle] (89) 3/4 - 10/2", str(rect))

    def test_update_kwarg_three(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=89, height=20, width=10)
        self.assertEqual("[Rectangle] (89) 3/4 - 10/20", str(rect))

    def test_update_kwarg_four(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=89, height=20, width=10, x=30)
        self.assertEqual("[Rectangle] (89) 30/4 - 10/20", str(rect))

    def test_update_kwarg_five(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=89, height=20, width=10, x=30, y=40)
        self.assertEqual("[Rectangle] (89) 30/40 - 10/20", str(rect))
if __name__ == '__main__':
    unittest.main()