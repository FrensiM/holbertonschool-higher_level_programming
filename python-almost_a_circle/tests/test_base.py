#!/usr/bin/python3
"""Test module"""
import io, sys, unittest, os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_no_args(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_none_id(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_three_base(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_id_uniq(self):
        self.assertEqual(20, Base(20).id)
    
    def test_id_pub(self):
        base1 = Base(15)
        base1.id = 20
        self.assertEqual(20, base1.id)

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_dict(self):
        self.assertEqual(str, type(Base.to_json_string([{'id': 12}])))

    def test_from_json_string_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_dict(self):
        self.assertEqual(list, type(Base.from_json_string('[{"id": 89}]')))

class TestBaseCreate(unittest.TestCase):
    def test_create_rectangle(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect_dict = rect.to_dictionary()
        rect2 = Rectangle.create(**rect_dict)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(rect2))

    def test_create_square(self):
        sq = Square(1, 2, 3, 4)
        sq_dict = sq.to_dictionary()
        sq2 = Square.create(**sq_dict)
        self.assertEqual("[Square] (4) 2/3 - 1", str(sq2))

class TestBaseSaveToFile(unittest.TestCase):
    # Delete created files
    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_rect(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_sq(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)
            
    def test_save_to_file_none_sq(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list_sq(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

class TestBaseLoadFrom(unittest.TestCase):
    # Delete created files
    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rect(self):
        rect1 = Rectangle(3, 4, 5, 6, 1)
        rect2 = Rectangle(7, 8, 9, 10, 2)
        Rectangle.save_to_file([rect1, rect2])
        list_rect = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(list_rect[0]))

    def test_load_from_file_second_rect(self):
        rect1 = Rectangle(3, 4, 5, 6, 1)
        rect2 = Rectangle(7, 8, 9, 10, 2)
        Rectangle.save_to_file([rect1, rect2])
        list_rect = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(list_rect[1]))

    def test_load_from_file_first_sq(self):
        sq1 = Square(3, 4, 5, 1)
        sq2 = Square(6, 7, 8, 2)
        Square.save_to_file([sq1, sq2])
        list_sq = Square.load_from_file()
        self.assertEqual(str(sq1), str(list_sq[0]))

    def test_load_from_file_second_sq(self):
        sq1 = Square(3, 4, 5, 1)
        sq2 = Square(6, 7, 8, 2)
        Square.save_to_file([sq1, sq2])
        list_sq = Square.load_from_file()
        self.assertEqual(str(sq2), str(list_sq[1]))

if __name__ == "__main__":
    unittest.main()