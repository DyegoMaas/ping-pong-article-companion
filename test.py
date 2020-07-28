import unittest

class FibonacciTests(unittest.TestCase):

    def test_o_primeiro_valor_eh_zero(self):
        valor = fibonacci(pos=0) # <-- essa função ainda nem existe!

        self.assertEqual(valor, 0)

if __name__ == '__main__':
    unittest.main()