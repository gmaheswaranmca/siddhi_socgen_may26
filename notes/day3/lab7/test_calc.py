# test_calc.py
import unittest
from calc import find_sum, find_diff

class TestCalc(unittest.TestCase):
    def test_find_sum(self):
        actual = find_sum(10, 20)
        expected = 30
        self.assertEqual(actual, expected)

    def test_find_diff(self):
        actual = find_diff(50, 20)
        expected = 30
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()