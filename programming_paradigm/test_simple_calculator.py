import unittest
from simple_calculator import SimpleCalculator

class TestCalculator:
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_add_positive(self):
        result=self.calc.add(4,3)
        self.assertEqual(result,7)
    def test_add_negative(self):
        result=self.calc.add(-2,5)
        self.assertEqual(result,3)
    def test_subtract_positive_result(self):
        result=self.calc.subtract(12,9)
        self.assertEqual(result,3)
    def test_subtract_negative_result(self):
        result=self.calc.subtract(-7,-4)
        self.assertEqual(result,-11)
    def test_subtract_positive(self):
        result=self.calc.subtract(4,2)
        self.assertEqual(result,2)
    def test_subtract_negative(self):
        result=self.calc.subtract(2,4)
        self.assertEqual(result,-2)
    def test_multiply(self):
        result=self.calc.multiply(4,2)
        self.assertEqual(result,8)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(2,0)
    def test_divide(self):
        result=self.calc.divide(4,2)
        self.assertEqual(result,2)
if __name__=="__main__":
    unittest.main()
    
