# Exercício de avaliação de expressão aritmética.
# Só podem ser usadas as estruturas Pilha e Fila implementadas em aulas anteriores.
# Deve ser análise de tempo e espaço para função avaliação
import operator
import string
import unittest
from itertools import chain
from numbers import Number

from aula_04.pilha_com_lista_duplamente_ligada import Pilha
from aula_05.fila import Fila


class ErroLexico(Exception):
    pass


class ErroSintatico(Exception):
    pass


caracteres_de_abertura = frozenset('{[(')
caracteres_de_fechamento = frozenset(']})')
operacoes = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}
caracteres_de_abertura_ou_fechamento = frozenset(chain(caracteres_de_abertura, caracteres_de_fechamento))

caracteres_nao_numericos = frozenset(chain(caracteres_de_abertura_ou_fechamento, operacoes.keys()))
caracteres_validos = frozenset(
    chain(caracteres_nao_numericos, '.', *string.digits))


def analise_lexica(expressao: str) -> Fila:
    """
    Executa análise lexica transformando a expressao em fila de objetos:
    e verificar se demais caracteres são validos: +-*/(){}[]
    :param expressao: string com expressao a ser analisada
    :return: fila com tokens
    """
    token = Fila()
    fila_de_tokens = Fila()
    for letra in expressao:
        if letra not in caracteres_validos:
            raise ErroLexico()

        if letra.isnumeric():
            token.enfileirar(letra)
        else:
            if not token.esta_vazia():
                fila_de_tokens.enfileirar(''.join(token))
                token = Fila()
            fila_de_tokens.enfileirar(letra)
    if not token.esta_vazia():
        fila_de_tokens.enfileirar(''.join(token))

    return fila_de_tokens


def analise_sintatica(fila: Fila) -> Fila:
    """
    Função que realiza analise sintática de tokens produzidos por analise léxica.
    Executa validações sintáticas e se não houver erro retorn fila_sintatica para avaliacao
    Transforma inteiros em ints
    Flutuantes em floats

    :param fila: fila proveniente de análise lexica
    :return: fila_sintatica com elementos tokens de numeros
    """
    if fila.esta_vazia():
        raise ErroSintatico()
    fila_de_valores_sintaticos = Fila()
    possivel_numero = Fila()
    for token in fila:
        if token in caracteres_nao_numericos:
            if len(possivel_numero) == 1 and token != '.':
                fila_de_valores_sintaticos.enfileirar(int(possivel_numero.desenfileirar()))
            elif len(possivel_numero) == 3:
                numero_str = ''.join(possivel_numero)
                fila_de_valores_sintaticos.enfileirar(float(numero_str))
                possivel_numero = Fila()
            fila_de_valores_sintaticos.enfileirar(token)
        else:
            possivel_numero.enfileirar(token)

    if len(possivel_numero) == 1:
        fila_de_valores_sintaticos.enfileirar(int(possivel_numero.desenfileirar()))
    elif len(possivel_numero) == 3:
        numero_str = ''.join(possivel_numero)
        fila_de_valores_sintaticos.enfileirar(float(numero_str))
    return fila_de_valores_sintaticos


def avaliar(expressao: str) -> Number:
    """
    Função que avalia expressão aritmetica retornando seu valor se não houver nenhum erro
    :param expressao: string com expressão aritmética
    :return: valor númerico com resultado
    """
    # Fazer análise léxica
    fila_lexica = analise_lexica(expressao)
    # Fazer análise sintática
    fila_sintatica = analise_sintatica(fila_lexica)
    # Processar os tokens gerados
    pilha_de_tokens = Pilha()
    pilha_de_tokens.empilhar(fila_sintatica.desenfileirar())
    if fila_sintatica.esta_vazia():
        return pilha_de_tokens.desempilhar()
    pilha_de_tokens.empilhar(fila_sintatica.desenfileirar())
    # 2 + 1
    for token in fila_sintatica:
        if token in caracteres_de_fechamento:
            numero = pilha_de_tokens.desempilhar()
            pilha_de_tokens.desempilhar()  # Caracter de abertura
            pilha_de_tokens.empilhar(numero)
        else:
            pilha_de_tokens.empilhar(token)
        calcular_operacoes_matematicas(pilha_de_tokens)

    return pilha_de_tokens.desempilhar()


def calcular_operacoes_matematicas(pilha_de_tokens):
    while len(pilha_de_tokens) > 2:
        segundo_operando = pilha_de_tokens.desempilhar()
        operacao = pilha_de_tokens.desempilhar()
        primeiro_operando = pilha_de_tokens.desempilhar()
        try:
            funcao_de_operacao = operacoes[operacao]
            resultado = funcao_de_operacao(primeiro_operando, segundo_operando)
        except (KeyError, TypeError):
            pilha_de_tokens.empilhar(primeiro_operando)
            pilha_de_tokens.empilhar(operacao)
            pilha_de_tokens.empilhar(segundo_operando)
            break
        else:
            pilha_de_tokens.empilhar(resultado)


class AnaliseLexicaTestes(unittest.TestCase):
    def test_expressao_esta_vazia(self):
        fila = analise_lexica('')
        self.assertTrue(fila.esta_vazia())

    def test_caracter_estranho(self):
        self.assertRaises(ErroLexico, analise_lexica, 'a')
        self.assertRaises(ErroLexico, analise_lexica, 'ab')

    def test_inteiro_com_um_algarismo(self):
        fila = analise_lexica('1')
        self.assertEqual('1', fila.desenfileirar())
        self.assertTrue(fila.esta_vazia())

    def test_inteiro_com_varios_algarismos(self):
        fila = analise_lexica('1234567890')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertTrue(fila.esta_vazia())

    def test_float(self):
        fila = analise_lexica('1234567890.34')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('34', fila.desenfileirar())
        self.assertTrue(fila.esta_vazia())

    def test_parenteses(self):
        fila = analise_lexica('(1)')
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertTrue(fila.esta_vazia())

    def test_chaves(self):
        fila = analise_lexica('{(1)}')
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertTrue(fila.esta_vazia())

    def test_colchetes(self):
        fila = analise_lexica('[{(1.0)}]')
        self.assertEqual('[', fila.desenfileirar())
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertEqual(']', fila.desenfileirar())
        self.assertTrue(fila.esta_vazia())

    def test_adicao(self):
        fila = analise_lexica('1+2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('+', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.esta_vazia())

    def test_subtracao(self):
        fila = analise_lexica('1-2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.esta_vazia())

    def test_multiplicacao(self):
        fila = analise_lexica('1*2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('*', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.esta_vazia())

    def test_divisao(self):
        fila = analise_lexica('1/2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('/', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.esta_vazia())

    def test_expresao_com_todos_simbolos(self):
        expressao = '1/{2.0+3*[7-(5-3)]}'
        fila = analise_lexica(expressao)
        self.assertListEqual(list(expressao), [e for e in fila])
        self.assertTrue(fila.esta_vazia())


class AnaliseSintaticaTestes(unittest.TestCase):
    def test_fila_esta_vazia(self):
        fila = Fila()
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_int(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.esta_vazia())

    def test_float(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila.enfileirar('.')
        fila.enfileirar('4')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890.4, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.esta_vazia())

    def test_expressao_com_todos_elementos(self):
        fila = analise_lexica('1000/{222.125+3*[7-(5-3)]}')
        fila_sintatica = analise_sintatica(fila)
        self.assertListEqual([1000, '/', '{', 222.125, '+', 3, '*', '[', 7, '-', '(', 5, '-', 3, ')', ']', '}'],
                             [e for e in fila_sintatica])


class AvaliacaoTestes(unittest.TestCase):
    def test_expressao_esta_vazia(self):
        self.assertRaises(ErroSintatico, avaliar, '')

    def test_inteiro(self):
        self.assert_avaliacao('1')

    def test_float(self):
        self.assert_avaliacao('2.1')

    def test_soma(self):
        self.assert_avaliacao('2+1')

    def test_subtracao_e_parenteses(self):
        self.assert_avaliacao('(2-1)')

    def test_expressao_com_todos_elementos(self):
        self.assertEqual(1.0, avaliar('2.0/[4*3+1-{15-(1+3)}]'))  # 2.0

    def assert_avaliacao(self, expressao):
        self.assertEqual(eval(expressao), avaliar(expressao))


if __name__ == '__main__':
    unittest.main()
