"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velociade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar a direita
3) Método girar a esquerda
  N
O   L
  S

    Exemplo:
>>> # Testando motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0
>>> # Testando direção
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.gerar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.gerar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.gerar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.gerar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.gerar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.gerar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.gerar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.gerar_a_esquerda()
>>> direcao.valor
'Norte'
>>> # Testando carro
>>> carro = Carrp(direcao, motor)
>>> carro.calcular_velocidade()
>>> 0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
>>> 1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
>>> 2
>>> carro.frear()
>>> carro.calcular_velocidade()
>>> 0
>>> carro.calcular_direcao()
>>> 'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
>>> 'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
>>> 'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
>>> 'Oeste'
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = max(self.velocidade - 2, 0)
