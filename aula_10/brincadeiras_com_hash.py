class Pessoa:
    def __init__(self, nome='Renzo'):
        self.nome = nome

    def __hash__(self):
        return hash(self.nome)

    def __eq__(self, outro):
        return self.nome == outro.nome

    def __repr__(self):
        return f'Pessoa({repr(self.nome)})'


vazio = Pessoa()
print(hash(vazio))
foo = Pessoa('Foo')
print(hash(foo))
dct = {foo: 'foo'}
print(dct)
print(f'Hash inicial de Foo: {hash(foo)}')
print(foo in dct)
print(vazio in dct)
foo.nome = 'Jorge'
print(f'Hash Final de Foo: {hash(foo)}')
print(foo in dct)
