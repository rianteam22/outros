hora = input('Insiras as horas (0 - 23): ')

if hora.isdigit():
    hora = int(hora)
    if 0 <= hora <= 23:
        if hora <= 11:
            print('Bom dia')
        elif hora <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
    else:
        print('digite um horario entre 0 e 23')
else:
    print('digite um horario valido')
