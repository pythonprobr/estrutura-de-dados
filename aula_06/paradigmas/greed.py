import unittest
from collections import defaultdict


def fabrica_de_zero():
    return 0


def calcular_troco(valor: int, tipos_de_notas=set):
    notas_ordendas = sorted(tipos_de_notas, reverse=True)
    frequencia = defaultdict(fabrica_de_zero)
    for nota in notas_ordendas:
        quantidade_de_notas, valor = divmod(valor, nota)
        if quantidade_de_notas > 0:
            frequencia[nota] = quantidade_de_notas
    return frequencia


class TestTroco(unittest.TestCase):
    def test_troco(self):
        self.assertDictEqual({}, calcular_troco(9, {10}))
        self.assertDictEqual({10: 1}, calcular_troco(10, {10}))
        self.assertDictEqual({10: 2, 5: 1, 1: 4}, calcular_troco(29, {1, 5, 10}))
        self.assertDictEqual({10: 1,  1: 4}, calcular_troco(14, {1, 7, 10}))
