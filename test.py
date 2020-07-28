import unittest
from unittest.mock import patch

def fibonacci(pos):
    if pos == 1:
        return 1
    return 0

class FibonacciTests(unittest.TestCase):

    def test_o_primeiro_valor_eh_zero(self):
        valor = fibonacci(pos=0) # <-- essa função ainda nem existe!

        self.assertEqual(valor, 0)

    def test_o_segundo_valor_eh_um(self):
        valor = fibonacci(pos=1)

        self.assertEqual(valor, 1)

    @patch('builtins.input', return_value=[(2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13)])
    def test_o_proximo_valor_eh_a_soma_dos_dois_anteriores(self, retornos):
        for par in retornos():
            posicao, valor_esperado = par
            valor = fibonacci(posicao)

            self.assertEqual(valor, valor_esperado)

if __name__ == '__main__':
    unittest.main()