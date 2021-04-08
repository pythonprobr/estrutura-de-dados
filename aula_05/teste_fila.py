import unittest

from aula_05.fila import Fila, FilaVaziaErro


class FilaTestes(unittest.TestCase):
    def test_primeiro_fila_esta_vazia(self):
        fila = Fila()
        self.assertTrue(fila.esta_vazia())
        self.assertRaises(FilaVaziaErro, fila.primeiro)
        self.assertEqual(0, len(fila))

    def test_enfileirar_um_elemento(self):
        fila = Fila()
        fila.enfileirar('A')
        self.assertFalse(fila.esta_vazia())
        self.assertEqual('A', fila.primeiro())

    def test_enfileirar_dois_elementos(self):
        fila = Fila()
        fila.enfileirar('A')
        fila.enfileirar('B')
        self.assertFalse(fila.esta_vazia())
        self.assertEqual('A', fila.primeiro())

    def test_desenfileirar_fila_esta_vazia(self):
        fila = Fila()
        self.assertRaises(FilaVaziaErro, fila.desenfileirar)

    def test_desenfileirar(self):
        fila = Fila()
        letras = 'ABCDE'
        for letra in letras:
            fila.enfileirar(letra)

        for letra in letras:
            letra_desenfileirada = fila.desenfileirar()
            self.assertEqual(letra, letra_desenfileirada)

    def test_iterar(self):
        fila = Fila()
        letras = 'ABCDE'
        for letra in letras:
            fila.enfileirar(letra)

        for letra, letra_desenfileirada in zip(letras, fila):
            self.assertEqual(letra, letra_desenfileirada)
        self.assertTrue(fila.esta_vazia())

    def test_tamanho(self):
        fila = Fila()
        letras = 'ABCDE'
        for tamanho, letra in enumerate(letras, start=1):
            fila.enfileirar(letra)
            assert tamanho == len(fila)
