contagem_de_chamadas_recursivas = 0


def _torre_de_hanoi_recursivo(numero_de_discos, origem, destino, auxiliar) -> object:
    """
    f(n) = 1 + 2 * f(n-1)
    f(n) = 1 + 2 * (1 + 2 * f(n-2)) -> 1 + 2 + 4*f(n-2)
    f(n) = 1 + 2 + 4 * ( 1 + 2 * f(n-3)) ->1 + 2 + 4 + 8* f(n-3)
    f(n) = 1 + 2 + 4 ... 2**(n-1)     (I)
    2 * f(n) = 2+ 4 + 8 ... 2 ** n    (II)
    f(n) = 2**n - 1                    II - I

    O(2**n) para tempo de execução

    O(n) para memória

    :param numero_de_discos:
    :param origem:
    :param destino:
    :param auxiliar:
    :return:
    """
    global contagem_de_chamadas_recursivas
    contagem_de_chamadas_recursivas += 1
    if numero_de_discos == 1:
        print(f'{origem} -> {destino} : {numero_de_discos}')
        return
    _torre_de_hanoi_recursivo(numero_de_discos - 1, origem, auxiliar, destino)
    print(f'{origem} -> {destino} : {numero_de_discos}')
    _torre_de_hanoi_recursivo(numero_de_discos - 1, auxiliar, destino, origem)


def torre_de_hanoi(numero_de_discos: int):
    global contagem_de_chamadas_recursivas
    contagem_de_chamadas_recursivas = 0
    _torre_de_hanoi_recursivo(numero_de_discos, origem='A', destino='B', auxiliar='C')


if __name__ == '__main__':
    for i in range(1, 4):
        print(f'##### Hanoi para {i} discos')
        torre_de_hanoi(i)
        print(f'********* {contagem_de_chamadas_recursivas} chamadas')
