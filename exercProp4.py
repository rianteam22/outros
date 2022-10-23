"""
Fizz Buzz - se o parametro da funcao for divisivel por 3, retorne fizz, se o parametro da funcao for divisivel por 5,
retorne buzz. se o parametro da funcao for divisivel por 5 e pro 3, retorne FizzBuzz, caso cotrario retorne o numero
enviado
"""


def fizzbuzz(numero):
    if(numero % 5) == 0 and (numero % 3) == 0:
        return 'FizzBuzz'
    if(numero % 5) == 0:
        return 'Buzz'
    if(numero % 3) == 0:
        return 'Fizz'
    return numero


while True:
    num = int(input('Numero: '))
    print(fizzbuzz(num))
