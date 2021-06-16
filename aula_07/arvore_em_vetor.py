"""
Representação em vetor de uma árvore binária

                                20
                    19                      10
                3      4               2       6
"""
from math import log

arvore = 'ABCDEFGH'


def calcular_indice_filho_esquerdo(indice_do_pai):
    return (indice_do_pai + 1) * 2 - 1


def calcular_indice_filho_direito(indice_do_pai):
    return calcular_indice_filho_esquerdo(indice_do_pai) + 1

def calcular_indice_pai(indice_do_filho):
    return (indice_do_filho-1) // 2

print('Filhos esquerdos')
for i, v in enumerate(arvore):
    indice_filho_esquerdo = calcular_indice_filho_esquerdo(i)
    try:
        filho_esquerdo = arvore[indice_filho_esquerdo]
    except IndexError:
        print(f'{v} é folha, sem filho esquerdo ')
    else:
        print(f'{v} tem filho esquerdo {filho_esquerdo}')


print('############## Filhos direitos')
for i, v in enumerate(arvore):
    indice_filho_direito = calcular_indice_filho_direito(i)
    try:
        filho_direito = arvore[indice_filho_direito]
    except IndexError:
        print(f'{v} é folha, sem filho direito ')
    else:
        print(f'{v} tem filho direito {filho_direito}')

print('############## Pais')
for i, v in enumerate(arvore):
    indice_pai = calcular_indice_pai(i)
    if indice_pai==-1:
        print(f'{v} não tem pai, pois é raiz')
    else:
        pai = arvore[indice_pai]
        print(f'{v} tem pai {pai}')


def calcular_altura(arvore):
    return len(arvore).bit_length() -1


altura = calcular_altura(arvore)
print('######### Algura')

print(altura)