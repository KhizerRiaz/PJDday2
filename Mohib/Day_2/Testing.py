import unittest
from Task_2 import StandardDeviation
class TestCircleArea(unittest.TestCase):
    # Check Answer Normally
    def test_area(self):
        self.assertAlmostEqual(StandardDeviation([1,2,3]),0.66666666)
        self.assertAlmostEqual(StandardDeviation([0,0,0]),0)
        self.assertAlmostEqual(StandardDeviation([-1,-1,-1]),0)
