class Noh:
    def __init__(self, valor, proximo=None):
        self.proximo = proximo
        self.valor = valor

    def __iter__(self):
        noh_atual = self
        while noh_atual != None:
            yield noh_atual
            noh_atual = noh_atual.proximo


class ListaLigadaSimples:
    def __init__(self):
        self._noh_inicial: Noh = None

    def __len__(self):
        if self._noh_inicial is None:
            return 0
        for indice, _ in enumerate(self._noh_inicial, start=1):
            pass
        return indice

    def __getitem__(self, indice_procurado):
        if self._noh_inicial is None:
            raise IndexError(f'Não existe valor para índice: {indice_procurado}')
        for indice, noh in enumerate(self._noh_inicial):
            if indice == indice_procurado:
                return noh.valor
        raise IndexError(f'Índice {indice_procurado} maior que o máximo: {indice}')

    def __iter__(self):
        for noh in self._noh_inicial:
            yield noh.valor

    def adicionar(self, valor, indice=None):
        if indice == 0:
            self._noh_inicial = Noh(valor, self._noh_inicial)
            return
        elif indice is None:
            noh = Noh(valor)
            if self._noh_inicial is None:
                self._noh_inicial = noh
            else:
                ultimo_noh = self._noh_inicial
                while ultimo_noh.proximo is not None:
                    ultimo_noh = ultimo_noh.proximo
                ultimo_noh.proximo = noh
        else:
            for indice_atual, noh_atual in enumerate(self._noh_inicial, start=1):
                if indice_atual == indice:
                    noh = Noh(valor, noh_atual.proximo)
                    noh_atual.proximo = noh
                    break