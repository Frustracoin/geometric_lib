import unittest
from square import area, perimeter

class test_square_area(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), 9)
        self.assertEqual(area(4), 16)
        self.assertEqual(area(5), 25)
        self.assertEqual(area(6), 36)
    def exception_test_area(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area(-3), 0)
    def unexpected_types_test_area(self):
        self.assertEqual(area("3"), 9)
        self.assertEqual(area("4"), 16)
        self.assertEqual(area("5"), 25)
        self.assertEqual(area("6"), 36)
        self.assertEqual(area([3]), 9)
        self.assertEqual(area([4]), 16)
        self.assertEqual(area([5]), 25)
        self.assertEqual(area([6]), 36)
    def overflow_test_area(self):
        self.assertEqual(area(1234567890987654321), 1524157877457704723228166437789971041)
    def unexpected_types_of_exceptions_test_area(self):
        self.assertEqual(area("0"), 0)
        self.assertEqual(area("-3"), 0)
        self.assertEqual(area([0]), 0)
        self.assertEqual(area([-3]), 0)
class test_square_perimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(3), 12)
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(6), 24)
    def exception_test_area(self):
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(-3), 0)
    def unexpected_types_test_area(self):
        self.assertEqual(perimeter("3"), 12)
        self.assertEqual(perimeter("4"), 16)
        self.assertEqual(perimeter("5"), 20)
        self.assertEqual(perimeter("6"), 24)
        self.assertEqual(perimeter([3]), 12)
        self.assertEqual(perimeter([4]), 16)
        self.assertEqual(perimeter([5]), 20)
        self.assertEqual(perimeter([6]), 24)
    def overflow_test_perimeter(self):
        self.assertEqual(perimeter(1234567890987654321), 4938271563950617284)
    def unexpected_types_of_exceptions_test_area(self):
        self.assertEqual(perimeter("0"), 0)
        self.assertEqual(perimeter("-3"), 0)
        self.assertEqual(perimeter([0]), 0)
        self.assertEqual(perimeter([-3]), 0)