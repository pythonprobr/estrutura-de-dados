from collections import deque
from unittest.case import TestCase


class Noh:
    def __init__(self, valor, pai: 'Noh' = None):
        self.valor = valor
        self.pai = None
        if pai:
            pai.adicionar(self)
        self.irmao_direito = None
        self.filho_esquerdo = None

    def adicionar(self, filho):
        if self.filho_esquerdo is None:
            self.filho_esquerdo = filho
        else:
            filho_sem_irmao_direito = self.filho_esquerdo
            while filho_sem_irmao_direito.irmao_direito is not None:
                filho_sem_irmao_direito = filho_sem_irmao_direito.irmao_direito
            filho_sem_irmao_direito.irmao_direito = filho
        filho.pai = self
    def __repr__(self):
        return repr(self.valor)

class Arvore:
    def __init__(self, raiz: Noh = None):
        self.raiz = raiz

    def altura(self):
        altura_maxima = 0
        altura_atual = 0
        pilha = deque()
        pilha.append((self.raiz, altura_atual))
        while pilha:
            noh_atual, altura_atual = pilha.pop()
            if noh_atual is None:
                continue
            pilha.append((noh_atual.irmao_direito, altura_atual))
            altura_atual += 1
            altura_maxima = max(altura_maxima, altura_atual)
            pilha.append((noh_atual.filho_esquerdo, altura_atual))
        return altura_maxima

    def __iter__(self):
        # pre ordem
        # pilha = deque()
        # pilha.append(self.raiz)
        # while pilha:
        #     noh_atual = pilha.pop()
        #     if noh_atual is None:
        #         continue
        #     yield noh_atual.valor
        #     pilha.append(noh_atual.irmao_direito)
        #     pilha.append(noh_atual.filho_esquerdo)


        pilha = deque()
        pilha.append((self.raiz, True))
        while pilha:
            noh_atual, procurar_filhos = pilha.pop()
            if noh_atual is None:
                continue
            if procurar_filhos:
                pilha.append((noh_atual.irmao_direito, True))
                pilha.append((noh_atual, False))
                pilha.append((noh_atual.filho_esquerdo, True))
            else:
                yield noh_atual.valor


class ArvoreTestes(TestCase):
    def teste_init(self):
        arvore = Arvore()
        self.assertIsNone(arvore.raiz)

    def teste_arvore_com_raiz(self):
        noh = Noh(1)
        arvore = Arvore(noh)
        self.assertIs(noh, arvore.raiz)

    def teste_altura_arvore(self):
        self.assertEqual(0, Arvore().altura())
        self.assertEqual(1, Arvore(Noh(1)).altura())
        arvore_binaria = self.gerar_arvore_binaria()
        self.assertEqual(4, arvore_binaria.altura())

    def test_travesia_em_profundidade(self):
        travessia_arvore_vazia = [i for i in Arvore()]
        self.assertListEqual([], travessia_arvore_vazia)
        travessia_arvore_unitaria = [i for i in Arvore(Noh(1))]
        self.assertListEqual([1], travessia_arvore_unitaria)
        arvore_binaria = self.gerar_arvore_binaria()
        travessia_arvore_binaria = [i for i in arvore_binaria]
        pos_ordem = [0, 1, 3, 4, 2, 6, 7, 9, 8, 5]
        pre_ordem = [5, 2, 1, 0, 4, 3, 8, 7, 6, 9]
        self.assertTrue(travessia_arvore_binaria == pos_ordem or travessia_arvore_binaria == pre_ordem)

    def gerar_arvore_binaria(self):
        """
                                    5
                      2                       8
                1         4             7          9
            0                 3     6
        
        :return:
        """
        nohs = [Noh(i) for i in range(10)]
        raiz = nohs[5]
        raiz.adicionar(nohs[2])
        raiz.adicionar(nohs[8])

        nohs[2].adicionar(nohs[1])
        nohs[2].adicionar(nohs[4])

        nohs[1].adicionar(nohs[0])

        nohs[4].adicionar(nohs[3])

        nohs[8].adicionar(nohs[7])
        nohs[8].adicionar(nohs[9])

        nohs[7].adicionar(nohs[6])

        return Arvore(raiz)


class NohTestes(TestCase):
    def teste_init_com_defaults(self):
        noh = Noh(5)
        self.assertEqual(5, noh.valor)
        self.assertIsNone(noh.pai)
        self.assertIsNone(noh.irmao_direito)
        self.assertIsNone(noh.filho_esquerdo)

    def teste_init_com_pai_justaposto(self):
        pai = Noh(5)
        filho = Noh(4, pai)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)

    def teste_init_com_pai_nomeado(self):
        pai = Noh(5)
        filho = Noh(4, pai=pai)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)

    def teste_adicionar_um_filho(self):
        pai = Noh(5)
        filho = Noh(4)
        pai.adicionar(filho)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)
        self.assertIsNone(filho.irmao_direito)

    def teste_adicionar_dois_filhos(self):
        pai = Noh(5)
        filho = Noh(4)
        filho2 = Noh(3)
        pai.adicionar(filho)
        pai.adicionar(filho2)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)
        self.assertIs(filho2, filho.irmao_direito)
        self.assertIsNone(filho2.irmao_direito)

    def teste_adicionar_tres_filhos(self):
        pai = Noh(5)
        filho = Noh(4)
        filho2 = Noh(3)
        filho3 = Noh(2)
        pai.adicionar(filho)
        pai.adicionar(filho2)
        pai.adicionar(filho3)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)
        self.assertIs(filho2, filho.irmao_direito)
        self.assertIs(filho3, filho2.irmao_direito)
        self.assertIsNone(filho3.irmao_direito)
