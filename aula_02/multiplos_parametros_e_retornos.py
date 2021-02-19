from random import shuffle


def gerar_ponto():
    return (1, 2, 3)


ponto = gerar_ponto()
print(type(ponto))
primeiro, *final = ponto  # desempacotamento
print(primeiro, final)


def argumentos_variaveis(*args):
    print(args)
    print(type(args))

argumentos_variaveis(1, 2)
argumentos_variaveis((1, 2))
argumentos_variaveis(*(1, 2))
argumentos_variaveis(*[1, 2])
argumentos_variaveis(*'ab')

for chave, valor in {'pt': 'Portugues', 'en': 'Ingles'}.items():
    print(chave, chave)


def ordenar(lista):
    lista= list(lista)
    lista.sort()
    return lista

numeros=list(range(10))
print(numeros)
shuffle(numeros)
print(numeros)
numeros_ordenados = ordenar(numeros)
print(numeros_ordenados)
print(numeros)
