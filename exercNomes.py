nome = input('Insira seu nome: ')

if nome.__len__() <= 4:
    print('seu nome eh curto')
elif nome.__len__() <= 6:
    print('seu nome eh normal')
else:
    print('seu nome eh muito grande')