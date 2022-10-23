# 123.456.789
cpfFinal = '06992132318'
cpf = cpfFinal[:9]
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

print(f'CPF Final = {cpfFinal}  CPF Calculado = {cpf}')
if cpf == cpfFinal:
    print('GG')
else:
    print('Sinto muito')