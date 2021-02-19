from array import array

vetor = array('h', [1, 2, 3, 4, 5])

print(type(vetor))
print(vetor)
print(vetor[0], vetor[-1])
vetor.append(6)
print(vetor[0], vetor[-1])
print(vetor)
vetor.append(2**15)
print(vetor[0], vetor[-1])
