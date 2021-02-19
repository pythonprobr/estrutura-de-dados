# Sequebncia Mutável:


lista = list()

print(id(lista))
print(lista)
lista.append(1)
print(id(lista))
print(lista)
print('### Soma de Lista')
print(id(lista))
lista = lista + [1]
print(id(lista))
print('### Extend de lista')
lista.extend([-2])
print(id(lista))

# Sequencias Imutáveis

tupla = (1, 3)
print(type(tupla))
print('### Soma de Tupla')
print(id(tupla))
tupla += (2, 4)
print(id(tupla))

print('### Soma de String')
a = 'Renzo'
print(id(a))
a += 'Nuccitelli'
print(id(a))
print(a.replace('e', '3'))
print(a)

print('### Sorted')
print(lista)
print(id(lista))
print(sorted(lista))
print(lista)

print('### Sort')
print(lista)
print(id(lista))
print(lista.sort())
print(lista)

print('### Objeto imutável mutante')

tupla = (lista,)
print(tupla)
print(id(tupla[0]))
lista.append(6)
print(tupla)
print(id(tupla[0]))
