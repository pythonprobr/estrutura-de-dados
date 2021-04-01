from aula_04.pilha_com_lista_duplamente_ligada import Pilha

CHAMADA_DE_FUNCAO = 'CHAMADA_DE_FUNCAO'
RETORNO_DE_FUNCAO = 'RETORNO_DE_FUNCAO'


def hanoi(numero_de_discos: int):
    """
    >>> hanoi(1)
    A -> B : 1
    >>> hanoi(2)
    A -> C : 1
    A -> B : 2
    C -> B : 1
    >>> hanoi(3)
    A -> B : 1
    A -> C : 2
    B -> C : 1
    A -> B : 3
    C -> A : 1
    C -> B : 2
    A -> B : 1

    Solução explicada em: https://youtu.be/X_ORc-byUkM

    :param numero_de_discos:
    :return:
    """
    origem = 'A'
    destino = 'B'
    auxiliar = 'C'

    pilha_de_execucao = Pilha()
    pilha_de_execucao.empilhar((CHAMADA_DE_FUNCAO, numero_de_discos, origem, destino, auxiliar))

    while not pilha_de_execucao.esta_vazia:
        operacao, numero_de_discos, origem, destino, auxiliar = pilha_de_execucao.desempilhar()
        if numero_de_discos == 1:
            print(f'{origem} -> {destino} : {numero_de_discos}')
            continue
        if operacao == CHAMADA_DE_FUNCAO:
            pilha_de_execucao.empilhar((RETORNO_DE_FUNCAO, numero_de_discos, origem, destino, auxiliar))
            pilha_de_execucao.empilhar((CHAMADA_DE_FUNCAO, numero_de_discos - 1, origem, auxiliar, destino))
        elif operacao == RETORNO_DE_FUNCAO:
            print(f'{origem} -> {destino} : {numero_de_discos}')
            pilha_de_execucao.empilhar((CHAMADA_DE_FUNCAO, numero_de_discos - 1, auxiliar, destino, origem))
