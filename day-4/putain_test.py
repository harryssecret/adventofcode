from main import count_contained_numbers, is_overlap, count_overlapping_numbers
import unittest


class CampCleanupTests(unittest.TestCase):

    def test_count_contained_numbers(self):
        self.assertEqual(count_contained_numbers("test_data.txt"), 2)
        self.assertEqual(count_contained_numbers("puzzle.txt"), 582)

    def test_is_overlapping(self):
        self.assertTrue(is_overlap([[25, 90], [60, 60]]))
        self.assertTrue(is_overlap([[60, 60], [25, 90]]))
        self.assertFalse(is_overlap([[30, 80], [100, 150]]))
        self.assertEqual(count_overlapping_numbers('test_data.txt'), 4)
