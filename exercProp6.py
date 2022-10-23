"""
Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada. Faca a funcao1 executar
duas duncoes que recebam um numero diferente de argumentos
"""


def mestre(func, *args, **kwargs):
    return func(*args, **kwargs)


def fala_oi(nome):
    return f'oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


exe = mestre(fala_oi, 'Rian')
exe2 = mestre(saudacao, 'Riann', saudacao='Fala')
print(exe)
print(exe2)
