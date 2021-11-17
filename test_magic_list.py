import unittest
from dataclasses import dataclass

from magic_list import MagicList


class Test(unittest.TestCase):

    def test_set_new_item_and_get_it(self):
        magic_list = MagicList()
        magic_list[0] = 5
        self.assertListEqual(magic_list, [5])
        assert magic_list[0] == 5

    def test_get_an_existing_item(self):
        magic_list = MagicList()
        magic_list[0] = 3
        magic_list[1] = 4
        magic_list[2] = 5

        assert magic_list[1] == 4

    def test_set_out_of_range_throws_exception(self):
        magic_list = MagicList()
        with self.assertRaises(IndexError):
            magic_list[1] = 5

    def test_assigned_type(self):
        @dataclass
        class Person:
            age: int = 1

        magic_list = MagicList(cls_type=Person)
        magic_list[0].age = 5
        assert magic_list[0].age == 5
