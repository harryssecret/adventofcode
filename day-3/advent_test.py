from main import find_item_priority, find_mistake
from part2 import create_elves_group, find_matching_char
import unittest


class TestAdventMethods(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.test_list = [
            ['vJrwpWtwJgWrhcsFMMfFFhFp',
                'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg'],
            ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
                'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
        ]

    def test_find_item_priority(self):
        self.assertEqual(find_item_priority("p"), 16)

    def test_find_mistakes(self):
        self.assertEqual(find_mistake("vJrwpWtwJgWrhcsFMMfFFhFp"), "p")
        self.assertEqual(find_mistake('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'), "L")
        self.assertEqual(find_mistake('PmmdzqPrVvPwwTWBwg'), "P")

    def test_list_splitting(self):
        self.assertEqual(create_elves_group('test_data.txt'), self.test_list)

    def test_find_duplicate_item(self):
        self.assertEqual(find_matching_char(self.test_list[0]), "r")
