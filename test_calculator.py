import unittest

from calculator import add, subtract, multiply, divide, power


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 4, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 0), 1)

    def test_power_zero_base_positive_exponent(self):
        self.assertEqual(power(0, 3), 0)

    def test_power_zero_base_negative_exponent(self):
        self.assertRaises(ZeroDivisionError, power, 0, -2)

    def test_power_negative_exponent(self):
        self.assertEqual(power(2, -2), 0.25)

    def test_power_negative_base_fractional_exponent(self):
        self.assertRaises(ValueError, power, -8, 0.5)


if __name__ == "__main__":
    unittest.main()
