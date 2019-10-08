from simple_calc import SimpleCalc
import unittest

class Calctest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2,4), 6)

    def test_subract(self):
        self.assertEqual(self.calc.subtract(6,4), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,2), 4)

    def test_divide(self):
        #   cal.divide(10,2) == 5
        self.assertEqual(self.calc.divide(10,2), 5)