import unittest

from src.calculator import add, divide, multiply, subtract


class TestCalculator(unittest.TestCase):

    def test_add(self):
        assert add(2, 3) == 5

    def test_subtract(self):
        assert subtract(5, 2) == 3

    def test_multiply(self):
        assert multiply(3, 4) == 12

    def test_divide(self):
        assert divide(10, 2) == 5

    def test_divide_by_zero(self):
        try:
            divide(10, 0)
        except ValueError:
            assert True
        else:
            assert False
