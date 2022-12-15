import unittest
from main import GiantCargo


class GiantCargoTests(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        cargo = GiantCargo()
        cargo.read_data_from_file("test_data.txt")
        cargo.parse_cargo()

    def test_giant_cargo_data_reading(self):
        self.assertListEqual(self.cargo.cargo, [[' ', 'D', ' '], ['N', 'C', ' '], [
                             'Z', 'M', 'P'], ['1', '2', '3']])

    def test_giant_cargo_instructions(self):
        self.assertListEqual(self.cargo.cargo, [[' ', ' ', 'Z'], [
                             ' ', ' ', 'N'], [' ', ' ', 'D'], ['C', 'M', 'P']])
