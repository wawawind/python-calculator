import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 2), 1)
    
    def test_sub(self):
        self.assertEqual(self.calc.subtract(3,2),1)
        self.assertEqual(self.calc.subtract(1,2),-1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3,2),6)
        self.assertEqual(self.calc.multiply(-3,2),-6)
        self.assertEqual(self.calc.multiply(3,-2),-6)
        self.assertEqual(self.calc.multiply(-3,-2),6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6,2),3)
        self.assertEqual(self.calc.divide(6,0), None)
        self.assertEqual(self.calc.divide(6,-2), -3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5,2),1)
        self.assertEqual(self.calc.modulo(6,2),0)
        self.assertEqual(self.calc.modulo(-5,2),1)
        self.assertEqual(self.calc.modulo(5,-2),1)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()