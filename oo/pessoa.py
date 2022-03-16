class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Leonardo', 25)
    print(id(p))
    print(p.cumprimentar())
    print(f'Nome: {p.nome}\nIdade: {p.idade}')
