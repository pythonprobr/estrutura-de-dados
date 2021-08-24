from collections import Counter

import unittest
from itertools import count


#   Solução ganancionada que não funciona
# def gerar_quadrados_perfeitos():
#     for i in count(0):
#         yield i ** 2
#
#
# def maior_quadrado_perfeito_menor_que(n: int):
#     quadrado_anterior = 0
#     for quadrado in gerar_quadrados_perfeitos():
#         if quadrado > n:
#             return quadrado_anterior
#         quadrado_anterior = quadrado
#
#
# def soma_quadrados(n: int):
#     quadrado_perfeito = maior_quadrado_perfeito_menor_que(n)
#     if quadrado_perfeito == n:
#         return [quadrado_perfeito]
#
#     novo_n = n-quadrado_perfeito
#     resultado = soma_quadrados(novo_n)
#     resultado.append(quadrado_perfeito)
#     return resultado
#

def gerar_quadrados_perfeitos_menores_ou_iguais_a(n: int):
    for i in count(1):
        quadrado = i ** 2
        if quadrado <= n:
            yield quadrado
        else:
            break


def soma_quadrados(n: int):
    if n == 0:
        return [0]
    return min(_gerar_todas_solucoes(n), key=len)


def _gerar_todas_solucoes(n: int):
    for quadrado in gerar_quadrados_perfeitos_menores_ou_iguais_a(n):
        if quadrado == n:
            yield [quadrado]
        novo_quadrado = n - quadrado
        for resultado in _gerar_todas_solucoes(novo_quadrado):
            resultado.append(quadrado)
            yield resultado


class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_1(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_2(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_3(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_4(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_5(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))

    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))
