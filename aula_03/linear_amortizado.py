from collections import Counter
from itertools import cycle
from time import perf_counter_ns

lista_de_numeros = list(range(10))
print(id(lista_de_numeros))
print(id(lista_de_numeros[0]))
print(id(lista_de_numeros[1]))
print(id(lista_de_numeros[2]))
lista_de_numeros.append(10)
maior_delta = 0
counter = Counter()

for i in cycle([11, 12]):
    id_final = id(lista_de_numeros)
    inicio = perf_counter_ns()
    lista_de_numeros.append(i)
    delta = perf_counter_ns() - inicio
    counter[delta // 200] += 1
    print(counter)
