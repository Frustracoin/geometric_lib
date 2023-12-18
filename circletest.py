import unittest
import math
from circle import area, perimeter

class test_circle_area(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), 28.274333882308138)
        self.assertEqual(area(4), 50.26548245743669)
        self.assertEqual(area(5), 78.53981633974483)
        self.assertEqual(area(6), 113.09733552923255)
    def unexpected_types_test_area(self):
        self.assertEqual(area("3"), 28.274333882308138)
        self.assertEqual(area("4"), 50.26548245743669)
        self.assertEqual(area("5"), 78.53981633974483)
        self.assertEqual(area("6"), 113.09733552923255)
        self.assertEqual(area([3]), 28.274333882308138)
        self.assertEqual(area([4]), 50.26548245743669)
        self.assertEqual(area([5]), 78.53981633974483)
        self.assertEqual(area([6]), 113.09733552923255)
    def test_overflow_area(self):
        self.assertEqual(area(63242397497234343), 1.2565116619999798e+34)
    def exceptions_test_area(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area(-3), 0)
    def unexpected_types_of_exceptions_test_area(self):
        self.assertEqual(area("0"), 0)
        self.assertEqual(area("-3"), 0)
        self.assertEqual(area([0]), 0)
        self.assertEqual(area([-3]), 0)
class test_circle_perimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(3), 18.84955592153876)
        self.assertEqual(perimeter(4), 25.132741228718345)
        self.assertEqual(perimeter(5), 31.41592653589793)
        self.assertEqual(perimeter(6), 37.69911184307752)
    def unexpected_types_test_perimeter(self):
        self.assertEqual(perimeter("3"), 18.84955592153876)
        self.assertEqual(perimeter("4"), 25.132741228718345)
        self.assertEqual(perimeter("5"), 31.41592653589793)
        self.assertEqual(perimeter("6"), 37.69911184307752)
        self.assertEqual(perimeter([3]), 18.84955592153876)
        self.assertEqual(perimeter([4]), 25.132741228718345)
        self.assertEqual(perimeter([5]), 31.41592653589793)
        self.assertEqual(perimeter([6]), 37.69911184307752)
    def test_overflow_perimeter(self):
        self.assertEqual(perimeter(1234567890987654321),7.757018833369319e+18)
    def exceptions_test_perimeter(self):
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(-3), 0)
    def unexpected_types_of_exceptions_test_perimeter(self):
        self.assertEqual(perimeter("0"), 0)
        self.assertEqual(perimeter("-3"), 0)
        self.assertEqual(perimeter([0]), 0)
        self.assertEqual(perimeter([-3]), 0)