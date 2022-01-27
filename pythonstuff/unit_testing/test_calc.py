# PyTest
from simplecalc import SimpleCalc
import pytest


@pytest.fixture
def calc():
    return SimpleCalc()


def test_calc_add(calc):
    # calc = SimpleCalc()
    assert calc.add(2, 6) != 7
    assert calc.add(-4, -0.84) == - 4.84
    assert calc.add(-6.5, -843.1) == -849.6


def test_calc_subtract(calc):
    # calc = SimpleCalc()
    assert calc.subtract(2, 6) == -4
    assert calc.subtract(-4, -0.84) == -3.16
    assert calc.subtract(-6.5, -843.1) == 836.6


def test_calc_multiply(calc):
    # calc = SimpleCalc()
    assert calc.multiply(2, 6) == 12
    assert calc.multiply(-4, 0.84) == -3.36
    assert calc.multiply(-6.5, -843.1) == 5480.15


def test_calc_divide(calc):
    # calc = SimpleCalc()
    assert calc.divide(2, 4) == 0.5
    assert calc.divide(-4, 0.84) == -4.761905
    assert calc.divide(-6.5, -843.1) == 0.007710


def test_calc_dividebyzero(calc):
    # calc = SimpleCalc()
    assert calc.divide(1, 0) == ZeroDivisionError

# class CalcTest(unittest.TestCase):
#     calc = SimpleCalc()
#
#     def test_add(self):
#         actual = self.calc.add(5, 10)
#         expected = 15
#         self.assertEqual(actual, expected)
#         actual = self.calc.add(-5, 10)
#         expected = 5
#         self.assertEqual(actual, expected)
#         actual = self.calc.add(-0.8, -19.3)
#         expected = -20.1
#         self.assertEqual(actual, expected)
#
#     def test_subtract(self):
#         actual = self.calc.subtract(5, 10)
#         expected = -5
#         self.assertEqual(actual, expected)
#         actual = self.calc.subtract(-5, 10)
#         expected = -15
#         self.assertEqual(actual, expected)
#         actual = self.calc.subtract(-0.8, -19.3)
#         expected = 18.5
#         self.assertEqual(actual, expected)
#         actual = self.calc.subtract(10, -5)
#         expected = 15
#         self.assertEqual(actual, expected)
#
#     def test_multiply(self):
#         actual = self.calc.multiply(5, 10)
#         expected = 50.0
#         self.assertEqual(actual, expected)
#         actual = self.calc.multiply(-3, 16)
#         expected = -48.0
#         self.assertEqual(actual, expected)
#         actual = self.calc.multiply(5.0, 10.90)
#         expected = 54.5
#         self.assertEqual(actual, expected)
#         actual = self.calc.multiply(0.4, -80.9)
#         expected = -32.36
#         self.assertEqual(actual, expected)
#
#     def test_divide(self):
#         actual = self.calc.divide(5, 10)
#         expected = 0.500
#         self.assertEqual(actual, expected)
#         actual = self.calc.divide(10, 5)
#         expected = 2.00
#         self.assertEqual(actual, expected)
#         actual = self.calc.divide(-5, 8)
#         expected = -0.625
#         self.assertEqual(actual, expected)
#         actual = self.calc.divide(0.8, 0.5)
#         expected = 1.600
#         self.assertEqual(actual, expected)

