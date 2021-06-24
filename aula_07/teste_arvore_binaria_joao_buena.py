"""
               A
      B                C
D         E      F         G
    >>> no_d=Arvore('D')
    >>> no_e=Arvore('E')
    >>> no_f=Arvore('F')
    >>> no_g=Arvore('G')
    >>> no_b=Arvore('B', no_d, no_e)
    >>> no_c=Arvore('C', no_f, no_g)
    >>> no_a=Arvore('A', no_b, no_c)
    >>> list(no_a)
    ['A', 'B', 'D', 'E', 'C', 'F', 'G']
"""


class _ArvoreNula:
    def __bool__(self):
        return False

    def __iter__(self):
        return iter('')


arvore_nula = _ArvoreNula()


class Arvore:
    def __init__(self, valor, filho_esquerdo: 'Arvore' = arvore_nula, filho_direito: 'Arvore' = arvore_nula):
        self.filho_direito = filho_direito
        self.filho_esquerdo = filho_esquerdo
        self.valor = valor

    def __iter__(self):
        yield self.valor
        yield from self.filho_esquerdo
        yield from self.filho_direito
