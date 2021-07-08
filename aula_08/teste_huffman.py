from collections import Counter
from typing import Union, Iterator
from unittest import TestCase


def calcular_frequencias(s):
    return Counter(s)


def gerar_arvore_de_huffman(s):
    frequencias = calcular_frequencias(s)
    arvores = [Arvore(char, peso) for char, peso in frequencias.items()]
    while len(arvores) > 1:
        arvores.sort(key=lambda arvore: arvore.raiz.peso, reverse=True)
        arvore_com_menor_frequencia = arvores.pop()
        arvore_com_segunda_menor_frequencia = arvores.pop()
        arvore_fundida = arvore_com_segunda_menor_frequencia.fundir(arvore_com_menor_frequencia)
        arvores.append(arvore_fundida)
    return arvores[0]


def codificar(cod_dict:dict, s:str):
    for char in s:
        yield cod_dict[char]



class Noh:
    def __init__(self, peso: int):
        self.peso = peso
        self.esquerdo = None
        self.direito = None

    def __hash__(self):
        return hash(self.peso)

    def __eq__(self, other):
        if other is None or not isinstance(other, Noh):
            return False
        return self.peso == other.peso and self.esquerdo == other.esquerdo and self.direito == other.direito


class Folha():
    def __init__(self, char: str, peso: int):
        self.peso = peso
        self.char = char

    def __hash__(self):
        return hash(self.__dict__)

    def __eq__(self, other):
        if other is None or not isinstance(other, Folha):
            return False
        return self.__dict__ == other.__dict__


def gerar_dicionario_de_codificao(noh: Union[Noh, Folha], resultado: dict, caminho: str):
    if isinstance(noh, Folha):
        resultado[noh.char] = caminho
    else:
        caminho_a_esquerda = caminho + '0'
        gerar_dicionario_de_codificao(noh.esquerdo, resultado, caminho_a_esquerda)
        caminho_a_direita = caminho + '1'
        gerar_dicionario_de_codificao(noh.direito, resultado, caminho_a_direita)

    return resultado


class Arvore(object):
    def __init__(self, char: str = None, peso: int = None):
        if char is None and peso is None:
            self.raiz = None
        else:
            self.raiz = Folha(char, peso)

    def __hash__(self):
        return hash(self.raiz)

    def __eq__(self, other):
        if other is None:
            return False
        return self.raiz == other.raiz

    def fundir(self, outra_arvore: 'Arvore'):
        noh = Noh(self.raiz.peso + outra_arvore.raiz.peso)
        noh.esquerdo = self.raiz
        noh.direito = outra_arvore.raiz
        arvore = Arvore()
        arvore.raiz = noh
        return arvore

    def cod_dict(self):
        return gerar_dicionario_de_codificao(self.raiz, {}, '')

    def decodificar(self, texto_codificado: str):
        return ''.join(decodificar(self.raiz, self.raiz, iter(texto_codificado)))


def decodificar(raiz: Union[Noh, Folha], noh: Union[Noh, Folha], iterator: Iterator[str]):
    if isinstance(noh, Folha):
        yield noh.char
        yield from decodificar(raiz, raiz, iterator)
    try:
        binario = next(iterator)
    except StopIteration:
        pass
    else:
        if binario == '0':
            yield from decodificar(raiz, noh.esquerdo, iterator)
        elif binario == '1':
            yield from decodificar(raiz, noh.direito, iterator)


class CalcularFrequenciaCarecteresTestes(TestCase):
    def teste_string_vazia(self):
        self.assertDictEqual({}, calcular_frequencias(''))

    def teste_string_nao_vazia(self):
        self.assertDictEqual({'a': 3, 'b': 2, 'c': 1}, calcular_frequencias('aaabbc'))


class NohTestes(TestCase):
    def teste_folha_init(self):
        folha = Folha('a', 3)
        self.assertEqual('a', folha.char)
        self.assertEqual(3, folha.peso)

    def teste_folha_eq(self):
        self.assertEqual(Folha('a', 3), Folha('a', 3))
        self.assertNotEqual(Folha('a', 3), Folha('b', 3))
        self.assertNotEqual(Folha('a', 3), Folha('a', 2))
        self.assertNotEqual(Folha('a', 3), Folha('b', 2))

    def testes_eq_sem_filhos(self):
        self.assertEqual(Noh(2), Noh(2))
        self.assertNotEqual(Noh(2), Noh(3))

    def testes_eq_com_filhos(self):
        noh_com_filho = Noh(2)
        noh_com_filho.esquerdo = Noh(3)
        self.assertNotEqual(Noh(2), noh_com_filho)

    def teste_noh_init(self):
        noh = Noh(3)
        self.assertEqual(3, noh.peso)
        self.assertIsNone(noh.esquerdo)
        self.assertIsNone(noh.direito)


def _gerar_arvore_aaaa_bb_c():
    raiz = Noh(7)
    raiz.esquerdo = Folha('a', 4)
    noh = Noh(3)
    raiz.direito = noh
    noh.esquerdo = Folha('b', 2)
    noh.direito = Folha('c', 1)
    arvore_esperada = Arvore()
    arvore_esperada.raiz = raiz
    return arvore_esperada


class ArvoreTestes(TestCase):
    def teste_init_com_defaults(self):
        arvore = Arvore()
        self.assertIsNone(arvore.raiz)

    def teste_init_sem_defaults(self):
        arvore = Arvore('a', 3)
        self.assertEqual(Folha('a', 3), arvore.raiz)

    def teste_fundir_arvores_iniciais(self):
        raiz = Noh(3)
        raiz.esquerdo = Folha('b', 2)
        raiz.direito = Folha('c', 1)
        arvore_esperada = Arvore()
        arvore_esperada.raiz = raiz

        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore_fundida = arvore.fundir(arvore2)
        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_fundir_arvores_nao_iniciais(self):
        arvore_esperada = _gerar_arvore_aaaa_bb_c()

        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore3 = Arvore('a', 4)
        arvore_fundida = arvore.fundir(arvore2)
        arvore_fundida = arvore3.fundir(arvore_fundida)

        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_gerar_dicionario_de_codificacao(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertDictEqual({'a': '0', 'b': '10', 'c': '11'}, arvore.cod_dict())

    def teste_decodificar(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))


class TestesDeIntegracao(TestCase):
    def teste_gerar_arvore_de_huffman(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual(arvore, gerar_arvore_de_huffman('aaaabbc'))

    def teste_codificar(self):
        arvore = gerar_arvore_de_huffman('aaaabbc')
        self.assertEqual('0000101011', ''.join(codificar(arvore.cod_dict(), 'aaaabbc')))
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))
