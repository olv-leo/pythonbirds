class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome, idade):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def metodo_de_classe(cls):
        return f'cls: {cls}, olhos: {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    leonardo = Homem(nome='Leonardo', idade=25)
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
    print(Pessoa.olhos)
    print(leonardo.olhos)
    print(dilma.olhos)
    leonardo.olhos = 3
    print(id(Pessoa.olhos), id(leonardo.olhos), id(dilma.olhos))
    print(leonardo.olhos)
    del leonardo.olhos
    print(id(Pessoa.olhos), id(leonardo.olhos), id(dilma.olhos))
    print(Pessoa.metodo_estatico(), Pessoa.metodo_de_classe())
    print(leonardo.metodo_estatico(), leonardo.metodo_de_classe())
    print(isinstance(leonardo, Pessoa))
    print(isinstance(dilma, Pessoa))
    print(isinstance(leonardo, Homem))
    print(isinstance(dilma, Homem))
    