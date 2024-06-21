import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(3, 5)
        self.assertEqual(result, 8)
        
        result = SimpleMath.addition(-1, 1)
        self.assertEqual(result, 0)
        
        result = SimpleMath.addition(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
