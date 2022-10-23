numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(numero, 'eh par')
    else:
        print(f'{numero} eh impar')
else:
    print('isso nao eh um numero inteiro')
