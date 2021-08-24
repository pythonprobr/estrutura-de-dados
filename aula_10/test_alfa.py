import unittest
from itertools import product

regra = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wzyz'}


def gerar_alfa(s: str):
    """
    Fazer análise de tempo e espaço
    Função recebe string com números de 2 a 9 e responde todas sequencias possíveis de letras
    Reg
    """
    yield from _gerar_alfa_rec(s, len(s) - 1)


def _gerar_alfa_rec(s, cursor):
    if cursor == -1:
        yield tuple()
        return

    for solucao_parcial_tpl in _gerar_alfa_rec(s, cursor - 1):
        for proxima_letra in regra[s[cursor]]:
            yield solucao_parcial_tpl + (proxima_letra,)


class Testes(unittest.TestCase):
    def testes_string_vazia(self):
        self.assertListEqual([tuple()], list(gerar_alfa('')))

    def testes_string_2(self):
        self.assertListEqual([('a',), ('b',), ('c',)], list(gerar_alfa('2')))

    def testes_string_3(self):
        self.assertListEqual([('d',), ('e',), ('f',)], list(gerar_alfa('3')))

    def testes_string_com_2_numeros(self):
        self.assertSetEqual(set((('a', 'd'), ('a', 'e'), ('a', 'f'), ('b', 'd'), ('b', 'e'), ('b', 'f'), ('c', 'd'),
                                 ('c', 'e'), ('c', 'f'))), set(gerar_alfa('23')))

    def testes_com_5_numeros(self):
        resultado = set(gerar_alfa('73696'))
        self.assertIn(tuple('renzo'), resultado)
        self.assertSetEqual(set(product('pqrs', 'def', 'mno', 'wzyz', 'mno')), resultado)
