import unittest

from aula_02.minmax import minmax


class TestMinMax(unittest.TestCase):
    def test_min_max_lista_com_um_elemento(self):
        resultado = minmax([1])
        self.assertEqual((1, 1), resultado)

    def test_min_max_lista_com_dois_elementos(self):
        resultado = minmax([1, 2])
        self.assertEqual((1, 2), resultado)

    def test_min_max_lista_vazia(self):
        with self.assertRaises(ValueError):
            minmax([])



