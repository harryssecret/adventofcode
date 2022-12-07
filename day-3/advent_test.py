from main import find_item_priority, find_mistake, find_good_rucksack
import unittest


class TestAdventMethods(unittest.TestCase):
    def test_find_item_priority(self):
        self.assertEqual(find_item_priority("p"), 16)

    def test_find_mistakes(self):
        self.assertEqual(find_mistake("vJrwpWtwJgWrhcsFMMfFFhFp"), "p")
        self.assertEqual(find_mistake('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'), "L")
        self.assertEqual(find_mistake('PmmdzqPrVvPwwTWBwg'), "P")
