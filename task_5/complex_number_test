import unittest
from complex_numbers import Complex_numbers


class TestComplexNumbers(unittest.TestCase):

    def test_add(self):
        number_1 = Complex(21, 2)
        number_2 = Complex(22, 3)
        expected = Complex(43, 5)

        actual = number_1 + number_2

        self.assertEqual(str(expected), str(actual))

    def test_sub(self):
        number_1 = Complex(16, 5)
        number_2 = Complex(12, 1)
        expected = Complex(4, 4)

        actual = number_1 - number_2

        self.assertEqual(str(expected), str(actual))

    def test_mul(self):
        number_1 = Complex(2, 3)
        number_2 = Complex(-1, 1)
        expected = Complex(-5, -1)

        actual = number_1 * number_2

        self.assertEqual(str(expected), str(actual))

    def test_truediv(self):
        number_1 = Complex(13, 1)
        number_2 = Complex(7, -6)
        expected = Complex(1.0, 1)

        actual = number_1 / number_2

        self.assertEqual(str(expected), str(actual))

    def test_abs(self):
        number = Complex(3, 4)
        expected = 5.0

        actual = abs(number)

        self.assertEqual(str(expected), str(actual))


if __name__ == "__main__":
    TestComplexNumbers()
