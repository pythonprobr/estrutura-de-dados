import unittest

from aula_03.lista_simples.lista_simples import Noh, ListaLigadaSimples
from aula_03.orientacao_a_objetos import Carro


class TesteNoh(unittest.TestCase):
    def test_criacao_de_noh_com_multiplos_objetos(self):
        for objeto in (1, 'Renzo', Carro('Chevete')):
            with self.subTest(objeto):
                noh = Noh(objeto)
                self.assertEqual(objeto, noh.valor)

    def test_proximo_noh_sem_inicializacao(self):
        noh = Noh(1)
        self.assertIsNone(noh.proximo)

    def test_proximo_noh_com_inicializacao(self):
        proximo = Noh(2)
        noh = Noh(1, proximo=proximo)

        self.assertIs(proximo, noh.proximo)


class TestListaLigadaSimples(unittest.TestCase):
    def test_criacao(self):
        lista_ligada = ListaLigadaSimples()
        self.assertEqual(0, len(lista_ligada))
        self.assertIsNone(lista_ligada._noh_inicial)

    def test_adicao_de_valor(self):
        lista_ligada = ListaLigadaSimples()
        lista_ligada.adicionar(1)
        self.assertEqual(1, len(lista_ligada))

    def test_acesso_primeiro_valor_lista_vazia(self):
        lista_ligada = ListaLigadaSimples()
        with self.assertRaises(IndexError):
            lista_ligada[0]

    def test_acesso_primeiro_valor(self):
        lista_ligada = ListaLigadaSimples()
        lista_ligada.adicionar(1)
        self.assertEqual(1, lista_ligada[0])

    def test_acesso_segundo_valor(self):
        lista_ligada = ListaLigadaSimples()
        lista_ligada.adicionar(1)
        lista_ligada.adicionar(2)
        self.assertEqual(1, lista_ligada[0])
        self.assertEqual(2, lista_ligada[1])

    def test_len_segundo_valor(self):
        lista_ligada = ListaLigadaSimples()
        lista_ligada.adicionar(1)
        lista_ligada.adicionar(2)
        self.assertEqual(2, len(lista_ligada))

    def test_indice_maior_que_o_maximo(self):
        lista_ligada = ListaLigadaSimples()
        lista_ligada.adicionar(1)
        lista_ligada.adicionar(2)
        with self.assertRaises(IndexError):
            lista_ligada[2]

    def test_iteracao_na_lista_ligada(self):
        lista_ligada = ListaLigadaSimples()
        lista_ligada.adicionar(1)
        lista_ligada.adicionar(2)
        self.assertListEqual([1, 2], list(lista_ligada))

    def test_iteracao_insercao_no_inicio(self):
        lista_ligada = ListaLigadaSimples()
        lista_ligada.adicionar(1)
        lista_ligada.adicionar(2, indice=0)
        self.assertListEqual([2, 1], list(lista_ligada))

    def test_iteracao_insercao_no_meio(self):
        lista_ligada = ListaLigadaSimples()
        lista_ligada.adicionar(1)
        lista_ligada.adicionar(2)
        lista_ligada.adicionar(3, indice=1)
        self.assertListEqual([1, 3, 2], list(lista_ligada))
        lista_ligada.adicionar(4, indice=1)
        self.assertListEqual([1, 4, 3, 2], list(lista_ligada))
