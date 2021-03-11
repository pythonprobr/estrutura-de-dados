class ListaVaziaErro(Exception):
    pass


class Noh():
    def __init__(self, valor, esquerdo=None, direito=None) -> None:
        '''
        Complexidade de Tempo:  f(n) = 3 -> O(1)
        Complexidade de Espaço: f(n) = 3 -> O(1)
        '''
        self.valor = valor
        self.esquerdo = esquerdo
        self.direito = direito

    def adicionar_a_direita(self, noh: 'Noh') -> 'Noh':
        self.direito = noh
        noh.esquerdo = self
        return noh

    def adicionar_a_esquerda(self, noh:'Noh'):
        noh.adicionar_a_direita(self)
        return noh


class ListaDuplamenteLigada():
    def __init__(self) -> None:
        '''
        Complexidade de Tempo:  f(n) = 3 -> O(1)
        Complexidade de Espaço: f(n) = 3 -> O(1)
        '''
        self.tam = 0
        self.primeiro = None
        self.ultimo = None

    def adicionar(self, valor):
        '''
        Complexidade de Tempo:  f(n) = 9 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        '''
        self.tam += 1
        noh = Noh(valor)
        if self.primeiro is None:
            self.ultimo = self.primeiro = noh
        else:
            self.ultimo = self.ultimo.adicionar_a_direita(noh)

    def adicionar_a_esquerda(self, valor):
        '''
        Complexidade de Tempo:  f(n) = 9 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        '''
        self.tam += 1
        noh = Noh(valor)
        if self.primeiro is None:
            self.ultimo = self.primeiro = noh
        else:
            self.primeiro = self.primeiro.adicionar_a_esquerda(noh)

    def remover(self):
        '''
        Complexidade de Tempo:  f(n) = 8 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        '''
        if self.primeiro is None:
            raise ListaVaziaErro('Não existem elementos na lista')
        elif self.ultimo is self.primeiro:
            noh = self.primeiro
            self.primeiro = None
            self.ultimo = None
        else:
            noh = self.ultimo
            self.ultimo = noh.esquerdo
            self.ultimo.direito = None
        self.tam -= 1
        return noh.valor

    def remover_a_esquerda(self):
        '''
        Complexidade de Tempo:  f(n) = 8 -> O(1)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        '''
        if self.primeiro is None:
            raise ListaVaziaErro('Não existem elementos na lista')
        elif self.ultimo is self.primeiro:
            noh = self.primeiro
            self.primeiro = None
            self.ultimo = None
        else:
            noh = self.primeiro
            self.primeiro = noh.direito
            self.primeiro.esquerdo = None
        self.tam -= 1
        return noh.valor

    def __iter__(self):
        '''
        Complexidade de Tempo:  f(n) = 3n + 1 -> O(n)
        Complexidade de Espaço: f(n) = 1 -> O(1)
        '''
        noh = self.primeiro
        while noh is not None:
            yield noh.valor
            noh = noh.direito
