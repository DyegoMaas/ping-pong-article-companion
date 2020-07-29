# O que é este repositório?

Este repositório representa uma sessão de ping-pong pair programming, em que a dupla vai implementar o algoritmo de **Fibonnacci usando TDD**.

## Como funciona?

Cada commit no histórico contém as alterações feitas pelo piloto na sua rodada. Os commits serão identificados como PING (commits de Fulano) ou PONG (commits de Ciclano), de acordo com o autor fictício do commit.

## O jogo do século

Nada melhor que um pouco código para ajudar a visualizar o processo de desenvolvimento com pareamento ping-pong. A seguir veremos o comecinho do processo de implementação de uma função para calcular a sequência de Fibonacci, codificada em Python.

A primeira atividade que a dupla (*Fulano e Ciclano*) deve executar, é entender a regra de negócio que pretende implementar. [Pesquisando na Wikipédia](https://pt.wikipedia.org/wiki/Sequência_de_Fibonacci), eles entendem que *a sequência de Fibonacci é uma sequência de números inteiros, que começa com 0 e 1, e cujo cada número subsequente é a soma dos dois anteriores*.

### Fulano começa (PING)

A dupla escolhe o piloto, e ele se responsibiliza por começar a implementação. Seguindo a boa prática de baby steps, ele implementa o menor teste que pode conceber:

```python
import unittest

class FibonacciTests(unittest.TestCase):

    def test_o_primeiro_valor_eh_zero(self):
        valor = fibonacci(pos=0) # <-- essa função ainda nem existe!

        self.assertEqual(valor, 0)

if __name__ == '__main__':
    unittest.main()
```

Sabendo que a regra dita que o primeiro valor retornado pela sequência é zero, o piloto escreveu um simples teste, que chama a futura função `fibonacci`, passando a `pos` 0, esperando que o valor retornado seja 0. Chegando ao fim da etapa `RED` do ciclo do TDD, ele passa a bola.

![Primeiro teste falhando](/img/exemplo-primeiro-teste-falhando.png")

### Ciclano assume (PONG)

Ciclano também está ciente dos baby steps, e escreve a menor implementação possível para fazer passar os testes, e chegar à fase `GREEN` do ciclo do TDD:

```python
def fibonacci(pos):
    return 0
```

Ele roda os testes, e está passando. Excelente.

![Primeiro teste passando](/img/exemplo-primeiro-teste-passando.png")

E então chega a hora de refatorar (etapa `REFACTOR`). Ele olha para Fulano, e chega à conclusão de que ainda é cedo pra isso, e parte para escrever o segundo teste:

```python
def test_o_segundo_valor_eh_um(self):
    valor = fibonacci(pos=1)

    self.assertEqual(valor, 1)
```

![Segundo teste falhando](/img/exemplo-segundo-teste-falhando.png")

Ele roda o teste, e o mesmo falha (`RED`). É hora de passar a bola. O código ficou assim:

```python
import unittest

def fibonacci(pos):
    return 0

class FibonacciTests(unittest.TestCase):

    def test_o_primeiro_valor_eh_zero(self):
        valor = fibonacci(0)

        self.assertEqual(valor, 0)

    def test_o_segundo_valor_eh_um(self):
        valor = fibonacci(pos=1)

        self.assertEqual(valor, 1)

if __name__ == '__main__':
    unittest.main()
```

### Fulano assume (PING)

Primeiro, ele faz o mínimo para o novo teste passar (`GREEN`):

```python
def fibonacci(pos):
    if pos == 1:
        return 1
    return 0
```

Essa foi rápida. Acabou o aquecimento. Os dois poderiam ficar nesse loop de adicionar um valor por vez por toda a eterninadade, mas isso não seria muito produtivo. É hora de deixar as coisas interessantes e **tacar lenha na fogueira!** Então Fulano escreve o próximo teste, forçando o colega a implementar uma versão do algoritmo que atenda os próximos valores da sequência (`RED`):

```python
from unittest.mock import patch

# ...

@patch('builtins.input', return_value=[(2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13)])
def test_o_proximo_valor_eh_a_soma_dos_dois_anteriores(self, retornos):
    for par in retornos():
        posicao, valor_esperado = par
        valor = fibonacci(posicao)

        self.assertEqual(valor, valor_esperado)
```

![Terceiro teste falhando](/img/exemplo-terceiro-teste-falhando.png")

### Ciclano assume (PONG)

Agora as coisas ficaram mais divertidas, e essa rodada talvez seja um pouco mais demorada. Após refletir por uns instantes, decide implementar o algoritmo com uma abordagem procedural, e chega neste resultado:

```python
def fibonacci(pos):
    anterior = 0
    proximo = 0

    for _ in range(0, pos):
        proximo = proximo + anterior
        anterior = proximo - anterior
        if(proximo == 0):
            proximo = proximo + 1
    
    return proximo
```

![Terceiro teste passando](/img/exemplo-terceiro-teste-passando.png")

Ele roda os testes e estão passando (`GREEN`). Ele decise refatorar levemente o código (`REFACTOR`), renomeando a variável `pos` para `posicao`. O código ficou assim:

```python
def fibonacci(posicao):
    anterior = 0
    proximo = 0

    for _ in range(0, posicao):
        proximo = proximo + anterior
        anterior = proximo - anterior
        if(proximo == 0):
            proximo = proximo + 1
    
    return proximo

# e os testes também:

def test_o_primeiro_valor_eh_zero(self):
    valor = fibonacci(posicao=0)

    self.assertEqual(valor, 0)

def test_o_segundo_valor_eh_um(self):
    valor = fibonacci(posicao=1)

    self.assertEqual(valor, 1)
```

O piloto está um pouco indeciso sobre qual teste escrever em seguida. Ele pergunta para o copiloto Fulano se tem alguma ideia, e o amigo o lembra que a sequência de Fibonacci só compreende números positivos. Eles decidem que nesses casos, a função deve retornar zero. Então Ciclano escreve este teste:

```python
def test_deve_retornar_zero_para_posicoes_negativas(self):
    valor = fibonacci(-1)

    self.assertEqual(valor, 0)
```

Ao rodar este teste, ele passa, porque coincidentemente o `for` não é processado. Então não conta como `RED` e ainda não pode passar a bola para o amigo.

![Quarto teste passando](/img/exemplo-quarto-teste-passando.png")

Olhando para o artigo na Wikipedia, ele decide que talvez não caiba escrever novos testes. Adiciona mais alguns casos no teste `test_o_proximo_valor_eh_a_soma_dos_dois_anteriores` e decide desafiar o colega a refatorar a função para a versão recursiva. O colega topa. Eles continuam na etapa `REFACTOR`.

### Fulano assume (PING)

Ele começa a refatorar a função, e chega a esta versão, que atende a todos os testes já escritos:

```python
def fibonacci(posicao):
    if posicao <= 0:
        return 0
    if posicao == 1:
        return 1
    else:
        return fibonacci(posicao - 1) + fibonacci(posicao - 2)
```

Os dois olham um para o outro com um aceno de que fizeram um bom trabalho. Fulano decide mover a função para um módulo `fib.py` e estão prontos. Já podem ir tomar um café. :)

O arquivo `fib.py` ficou assim:

```python
def fibonacci(posicao):
    if posicao <= 0:
        return 0
    if posicao == 1:
        return 1
    else:
        return fibonacci(posicao - 1) + fibonacci(posicao - 2)
```

E o arquivo de testes ficou assim:

```python
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
```