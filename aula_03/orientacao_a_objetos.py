class Carro:
    def __init__(self, nome):
        print('Chamando __init__')
        self.nome = nome

    def acelerar(self):
        return id(self)


if __name__ == '__main__':
    monza = Carro('Monza')
    print(id(monza), monza.acelerar(), Carro.acelerar(monza))
    chevete = Carro('Chevete')
    print(id(chevete), chevete.acelerar(), Carro.acelerar(chevete))
    # chevete.nome = 'Chevete'
    print(chevete.nome)
    print(monza.nome)
