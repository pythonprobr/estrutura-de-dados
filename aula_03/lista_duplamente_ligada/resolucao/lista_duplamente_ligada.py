class ListaVaziaErro(Exception):
    pass


class Noh():
    def __init__(self, valor, esquerdo=None, direito=None) -> None:
        '''
        Complexidade de Tempo:  f(n) = 3 -> O(1)
        Complexidade de Espaço: f(n) = 3 -> O(1)
        '''
        self.valor = valor
        self.esquerdo = noh_none if esquerdo is None else esquerdo
        self.direito = noh_none if direito is None else direito

    def adicionar_a_direita(self, noh: 'Noh') -> 'Noh':
        self.direito = noh
        noh.esquerdo = self
        return noh

    def adicionar_a_esquerda(self, noh: 'Noh'):
        noh.adicionar_a_direita(self)
        return noh

    def __iter__(self):
        noh = self
        while noh is not noh_none:
            yield noh
            noh = noh.direito

    def desfazer_ligacoes(self):
        direito = self.direito
        esquerdo = self.esquerdo
        direito.esquerdo = esquerdo.direito = self.direito = self.esquerdo = noh_none

    def remover_a_esquerda(self):
        self.esquerdo.direito = noh_none
        self.esquerdo = noh_none
        return self

    def calcular_primeiro(self, noh):
        return self

    def calcular_ultimo(self, noh):
        return self

    def calcular_primeiro_antes_da_remocao(self, ultimo_noh):
        if ultimo_noh is self:
            return noh_none
        return self


class _NohNoneObject(Noh):
    def __init__(self) -> None:
        '''
        Complexidade de Tempo:  f(n) = 3 -> O(1)
        Complexidade de Espaço: f(n) = 3 -> O(1)
        '''
        # self.esquerdo = esquerdo
        # self.direito = direito

    def calcular_primeiro(self, noh):
        return noh

    def calcular_ultimo(self, noh):
        return noh

    def desfazer_ligacoes(self):
        raise ImpossivelDesfazerLigacacoNohNone()



noh_none = _NohNoneObject()


class ImpossivelDesfazerLigacacoNohNone(Exception):
    pass


class ListaDuplamenteLigada():
    def __init__(self) -> None:
        '''
        Complexidade de Tempo:  f(n) = 3 -> O(1)
        Complexidade de Espaço: f(n) = 3 -> O(1)
        '''
        self.tam = 0
        self.primeiro = noh_none
        self.ultimo = noh_none

    def adicionar(self, valor):
        '''
        Complexidade de Tempo:  f(n) = 9 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        '''
        self.tam += 1
        noh = Noh(valor)
        self.primeiro = self.primeiro.calcular_primeiro(noh)
        self.ultimo = self.ultimo.adicionar_a_direita(noh)

    def adicionar_a_esquerda(self, valor):
        '''
        Complexidade de Tempo:  f(n) = 9 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        '''
        self.tam += 1
        noh = Noh(valor)
        self.ultimo = self.ultimo.calcular_ultimo(noh)
        self.primeiro = self.primeiro.adicionar_a_esquerda(noh)

    def remover(self):
        '''
        Complexidade de Tempo:  f(n) = 8 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        '''

        noh = self.ultimo
        self.ultimo = noh.esquerdo
        self.primeiro = self.primeiro.calcular_primeiro_antes_da_remocao(noh)
        try:
            noh.desfazer_ligacoes()
        except ImpossivelDesfazerLigacacoNohNone as e:
            raise ListaVaziaErro('Não existem elementos na lista') from e
        self.tam -= 1
        return noh.valor

    def remover_a_esquerda(self):
        '''
        Complexidade de Tempo:  f(n) = 8 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        '''
        if self.primeiro is noh_none:
            raise ListaVaziaErro('Não existem elementos na lista')
        elif self.ultimo is self.primeiro:
            noh = self.primeiro
            self.primeiro = noh_none
            self.ultimo = noh_none
        else:
            noh = self.primeiro
            self.primeiro = self.primeiro.direito.remover_a_esquerda()
        self.tam -= 1
        return noh.valor

    def __iter__(self):
        '''
        Complexidade de Tempo:  f(n) = 3n + 1 -> O(n)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        '''

        for noh in self.primeiro:
            yield noh.valor

