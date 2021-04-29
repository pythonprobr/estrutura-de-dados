import unittest


def ordenar(seq):
    lista_ordenada = []
    for indice, valor in enumerate(seq):
        indice_ordenado=0
        for indice_ordenado, valor_ordenado in enumerate(lista_ordenada):
            if valor_ordenado > valor:
                break
        lista_ordenada.insert(indice_ordenado, valor)

    return lista_ordenada


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], ordenar([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], ordenar([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], ordenar([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ordenar([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
