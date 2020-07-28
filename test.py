import unittest

def fibonacci(pos):
    return 0

class FibonacciTests(unittest.TestCase):

    def test_o_primeiro_valor_eh_zero(self):
        valor = fibonacci(pos=0) # <-- essa função ainda nem existe!

        self.assertEqual(valor, 0)

    def test_o_segundo_valor_eh_um(self):
        valor = fibonacci(pos=1)

        self.assertEqual(valor, 1)

if __name__ == '__main__':
    unittest.main()