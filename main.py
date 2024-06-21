import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b
    
    @staticmethod
    def subtraction(a, b):
        return a - b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(3, 5)
        self.assertEqual(result, 8)
        
        result = SimpleMath.addition(-1, 1)
        self.assertEqual(result, 0)
        
        result = SimpleMath.addition(0, 0)
        self.assertEqual(result, 0)
    
    def test_subtraction(self):
        result = SimpleMath.subtraction(5, 3)
        self.assertEqual(result, 2)
        
        result = SimpleMath.subtraction(-1, 1)
        self.assertEqual(result, -2)
        
        result = SimpleMath.subtraction(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()

