"""
Crie uma funcao que receba 2 numeros. o primeiro e um valor e o segundo um percentual (ex. 10%). retorne o valor do
primeiro numeor somado do aumento percentual do mesmo
"""


def aumento(num, perc):
    return num*(1+(perc/100))


numero = int(input('Digite um numero: '))
percentual = int(input('Digite um percentual de aumento: '))
print(f'aumento percentual de {percentual}% em R${numero:.2f} eh R${aumento(numero, percentual):.2f}')
