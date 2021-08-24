import time
from functools import cache

contagem = 0


@cache
def fib(n: int) -> int:
    global contagem
    contagem += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    for n in range(50):
        contagem = 0
        inicio = time.time()
        print(f'fib({n}) = {fib(n)}')
        fim = time.time() - inicio
        print(f'#### {contagem} chamadas')
        print(f'#### clock {fim}')
