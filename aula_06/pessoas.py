from builtins import NotImplementedError
from functools import total_ordering


@total_ordering
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.altura = altura
        self.idade = idade
        self.nome = nome

    def __repr__(self):
        return repr((self.nome, self.idade, self.altura))

    def __gt__(self, other):
        return self.altura > other.altura

    def __eq__(self, other):
        return self.altura == other.altura


pessoas = [
    Pessoa('Renzo', 38, 162),
    Pessoa('Thiago', 29, 192),
    Pessoa('Jorge', 62, 167),
    Pessoa('Walison', 27, 183),
    Pessoa('Gabriel', 27, 167),
]

renzo, thiago = pessoas[:2]
print(renzo > thiago)
print(renzo <= thiago)

print('Comparação entre tuplas: ', (166, 'Jorge') < (167, 'Gabriel'))
print('Ordenação por método mágico __gt__ da classe Pessoa reverso')
pessoas.sort(reverse=True)
print(pessoas)


def ordenar_por_idade_nome_altura(pessoa):
    return (pessoa.idade, pessoa.nome, pessoa.altura)


pessoas.sort(key=ordenar_por_idade_nome_altura)

print('Odenação por idade, nome e altura:')
print(pessoas)
