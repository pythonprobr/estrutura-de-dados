import unittest
from collections import defaultdict
from math import inf
from typing import Dict


def fabrica_de_zero():
    return 0

solucao_impossivel = defaultdict(fabrica_de_zero)
solucao_impossivel[-1] = inf


def calcular_melhor_solucao(solucao: Dict[int, int], outra_solucao: Dict[int, int]):
    if sum(solucao.values()) < sum(outra_solucao.values()):
        return solucao
    return outra_solucao


def calcular_troco_recursivo(valor: int, tipos_de_notas: set, solucao_parcial: Dict[int, int]):
    if valor == 0:
        return solucao_parcial
    elif valor < 0 or len(tipos_de_notas) == 0:
        return solucao_impossivel
    tipos_de_nota_sem_nota_escolhida = set(tipos_de_notas)
    nota_escolhida = tipos_de_nota_sem_nota_escolhida.pop()

    possivel_solucao = defaultdict(fabrica_de_zero)
    possivel_solucao.update(solucao_parcial)
    possivel_solucao[nota_escolhida] += 1

    solucao_com_nota_escolhida = calcular_troco_recursivo(valor - nota_escolhida, tipos_de_notas, possivel_solucao)
    solucao_sem_nota_escolhida = calcular_troco_recursivo(valor, tipos_de_nota_sem_nota_escolhida, solucao_parcial)

    return calcular_melhor_solucao(solucao_com_nota_escolhida, solucao_sem_nota_escolhida)


def calcular_troco(valor: int, tipos_de_notas):
    solucao_inicial = defaultdict(fabrica_de_zero)
    return calcular_troco_recursivo(valor, tipos_de_notas, solucao_inicial)


class TestTroco(unittest.TestCase):
    def test_troco(self):
        self.assertDictEqual(solucao_impossivel, calcular_troco(9, {10}))
        self.assertDictEqual({10: 1}, calcular_troco(10, {10}))
        self.assertDictEqual({10: 2, 5: 1, 1: 4}, calcular_troco(29, {1, 5, 10}))
        self.assertDictEqual({7: 2}, calcular_troco(14, {1, 7, 10}))
        self.assertDictEqual({7: 1, 10: 1}, calcular_troco(17, {1, 7, 10}))
