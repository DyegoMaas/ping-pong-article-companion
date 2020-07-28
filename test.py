import unittest
from unittest.mock import patch
from fib import fibonacci

class FibonacciTests(unittest.TestCase):

    def test_o_primeiro_valor_eh_zero(self):
        valor = fibonacci(posicao=0)

        self.assertEqual(valor, 0)

    def test_o_segundo_valor_eh_um(self):
        valor = fibonacci(posicao=1)

        self.assertEqual(valor, 1)

    @patch('builtins.input', return_value=[
        (2, 1), (3, 2), (4, 3), (5, 5), (6, 8),
        (7, 13), (8, 21), (9, 34), (10, 55)])
    def test_o_proximo_valor_eh_a_soma_dos_dois_anteriores(self, retornos):
        for par in retornos():
            posicao, valor_esperado = par
            valor = fibonacci(posicao)

            self.assertEqual(valor, valor_esperado)

    def test_deve_retornar_zero_para_posicoes_negativas(self):
        valor = fibonacci(-1)

        self.assertEqual(valor, 0)

if __name__ == '__main__':
    unittest.main()