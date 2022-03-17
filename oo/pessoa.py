class Pessoa:
    def __init__(self, *filhos, nome, idade):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    leonardo = Pessoa(nome='Leonardo', idade=25)
    dilma = Pessoa(leonardo, nome='Dilma', idade=40)
    print(leonardo.cumprimentar())
    print(f'Nome: {dilma.nome}\nIdade: {dilma.idade}\nFilhos:')
    for filho in dilma.filhos:
        print(filho.nome)

    leonardo.sobrenome = 'Oliveira'
    dilma.sobrenome = 'Cardoso'
    print(dilma.sobrenome)
    del dilma.sobrenome
    print(leonardo.__dict__)
    print(dilma.__dict__)
