"""
Crie uma funcao1 que recebbe uma funcao2 como parametro e retone o valor da funcao2 executada
"""


def funcao1(func):
    return func


def funcao2():
    print('deu certo')


funcao1(funcao2())