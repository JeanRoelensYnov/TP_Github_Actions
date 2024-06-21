import unittest

class SimpleMath:
    """Classe contenant des méthodes de mathématiques simples."""
    @staticmethod
    def addition(a, b):
        """Retourne la somme de a et b."""
        return a + b
    @staticmethod
    def subtraction(a, b):
        """Retourne la différence entre a et b."""
        return a - b

class TestSimpleMath(unittest.TestCase):
    """Classe de test pour les méthodes de SimpleMath."""
    def test_addition(self):
        """Teste la méthode addition."""
        result = SimpleMath.addition(3, 5)
        self.assertEqual(result, 8)
        result = SimpleMath.addition(-1, 1)
        self.assertEqual(result, 0)
        result = SimpleMath.addition(0, 0)
        self.assertEqual(result, 0)
    def test_subtraction(self):
        """Teste la méthode subtraction."""
        result = SimpleMath.subtraction(5, 3)
        self.assertEqual(result, 2)
        result = SimpleMath.subtraction(-1, 1)
        self.assertEqual(result, -2)
        result = SimpleMath.subtraction(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
