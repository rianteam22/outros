from random import randint

cpfInicial = str(randint(000000000, 999999999))
cpf = cpfInicial[:9]
cont = 10
while True:
    ac = 0
    for i, j in enumerate(range(cont, 1, -1)):
        ac += (int(cpf[i]) * j)
    ac = 11 - (ac % 11)
    cpf = cpf + '0' if (ac > 9) else cpf + str(ac)
    if cont == 11:
        break
    cont = 11

print(f'CPF inicial = {cpfInicial}  CPF Calculado = {cpf}')
