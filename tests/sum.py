import unittest


# La función que queremos probar
def sum(a, b):
    return a + b


# Definición de la clase de prueba
class TestSum(unittest.TestCase):

    # Método de prueba para verificar la suma de dos números positivos
    def test_sum_positive(self):
        result = sum(3, 5)
        self.assertEqual(result, 8)  # Verifica que 3 + 5 sea igual a 8

    # Método de prueba para verificar la suma de dos números negativos
    def test_sum_negatives(self):
        result = sum(-4, -6)
        self.assertEqual(result, -10)  # Verifica que (-4) + (-6) sea igual a -10


if __name__ == '__main__':
    unittest.main()
