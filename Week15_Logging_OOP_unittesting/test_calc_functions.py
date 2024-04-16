import unittest
import calc_functions


# inheriting TestCase from unittest module
class TestCalcFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc_functions.add(10, 5), 15)
        self.assertEqual(calc_functions.add(1, 1), 2)
        self.assertEqual(calc_functions.add(9, 7), 16)

    def test_subtract(self):
        self.assertEqual(calc_functions.subtract(4, 3), 1)
        self.assertEqual(calc_functions.subtract(14, 13), 1)
        self.assertEqual(calc_functions.subtract(8, 2), 6)

    def test_multiply(self):
        self.assertEqual(calc_functions.multiply(10, 10), 100)
        self.assertEqual(calc_functions.multiply(4, 6), 24)
        self.assertEqual(calc_functions.multiply(8, 2), 16)

    def test_divide(self):
        self.assertEqual(calc_functions.divide(2, 1), 2)
        self.assertEqual(calc_functions.divide(14, 2), 7)
        self.assertEqual(calc_functions.divide(48, 8), 6)


if __name__ == "__main__":
    unittest.main()
