"""
Crie uma fincao que exibe uma saudacao com os parametros saudacao e nome
"""


def impressao(saudacao, nome):
    return f'{saudacao}, {nome}'


nm = input('Diga seu nome: ')
print(impressao(saudacao='OLA', nome=nm))
