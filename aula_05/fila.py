from collections import deque


class FilaVaziaErro(Exception):
    pass


class Fila:
    def __init__(self):
        self._deque = deque()

    def esta_vazia(self):
        return not bool(self._deque)

    def primeiro(self):
        try:
            return self._deque[0]
        except IndexError as e:
            raise FilaVaziaErro() from e

    def __len__(self):
        return len(self._deque)

    def enfileirar(self, valor):
        self._deque.append(valor)

    def desenfileirar(self):
        try:
            return self._deque.popleft()
        except IndexError as e:
            raise FilaVaziaErro() from e

    def __iter__(self):
        while not self.esta_vazia():
            yield self.desenfileirar()
