import unittest


def quick_sort(seq):
    if len(seq) <=1:
        return seq
    pivot = seq.pop()
    menores = [n for n in seq if n < pivot]
    lista_ordenada = quick_sort(menores)
    lista_ordenada.append(pivot)
    maiores = [n for n in seq if n >= pivot]
    lista_ordenada.extend(quick_sort(maiores))
    return lista_ordenada




class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quick_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quick_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quick_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
    # inicial=0 final=9  = pivot
    # [9, 7, 1, 8, 5, 3, 6, 4, 2, 0]
    # Passo 1: trocar indice final com indice do pivo
    # inicio=0 pivot=9 final=8
    # [9, 7, 1, 8, 0, 3, 6, 4, 2, 5]
    # Passo 2 incrementar inicio até encontrar valor que seja maior que o valor do pivot
    # inicio = 1 pivot = 0 final = 8
    # [5, 7, 1, 8, 0, 3, 6, 4, 2, 9]
    # Passo 3: decrementar valor de indice final até encontrar valor menor que o pivot
    # inicio = 1 pivot = 8 final = 7
    # [2, 7, 1, 8, 0, 3, 6, 4, 5, 9]
    # Refazer passo 2
    # inicio = 5 pivot = 5 final = 5
    # [2, 4, 1, 3, 0, 5, 6, 8, 7, 9]
    # repetir inicio = 0  fim = 4 pivot= 2
    # repetir inicio= 6 fim=9
