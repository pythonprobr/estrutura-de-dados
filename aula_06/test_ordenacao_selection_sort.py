import unittest


def selection_sort(seq):
    for indice_atual, _ in enumerate(seq):
        indice_do_valor_minimo = min(
            (valor, indice) for indice, valor in
            enumerate(gerar_slice_sem_gastar_memoria(indice_atual, seq), start=indice_atual)
        )[1]
        seq[indice_atual], seq[indice_do_valor_minimo] = seq[indice_do_valor_minimo], seq[indice_atual]
    return seq


def gerar_slice_sem_gastar_memoria(indice_atual, seq):
    for indice in range(indice_atual, len(seq)):
        yield seq[indice]


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], selection_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], selection_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], selection_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], selection_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
