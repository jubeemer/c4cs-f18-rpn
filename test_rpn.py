import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)

    def test_subtract(self):
        result = rpn.calculate("4 3 -")
        self.assertEqual(1, result)

    def test_mul(self):
        result = rpn.calculate("4 3 *")
        self.assertEqual(12, result)

    def test_div(self):
        result = rpn.calculate("4 2 /")
        self.assertEqual(2, result)

    def test_exp(self):
        result = rpn.calculate("2 3 ^")
        self.assertEqual(8, result)

    def test_chain(self):
        result = rpn.calculate("1 1 + 2 *")
        self.assertEqual(4, result)
