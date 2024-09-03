# test_math_ops.py

import unittest
from math_ops import MathOps 

class TestMathOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(MathOps.add(2, 3), 5)
        self.assertEqual(MathOps.add(-1, 1), 0)
        self.assertEqual(MathOps.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(MathOps.subtract(5, 3), 2)
        self.assertEqual(MathOps.subtract(1, 1), 0)
        self.assertEqual(MathOps.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(MathOps.multiply(2, 3), 6)
        self.assertEqual(MathOps.multiply(-2, 3), -6)
        self.assertEqual(MathOps.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(MathOps.divide(6, 3), 2)
        self.assertEqual(MathOps.divide(7, 2), 3.5)
        self.assertRaises(ValueError, MathOps.divide, 1, 0)

if __name__ == '__main__':
    unittest.main()