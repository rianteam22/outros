secreto = 'paralelepipedo'
lista_letras = []
chances = 3

while True:
    if chances == 0:
        print('\nVoce perdeu\n')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra')
    else:
        lista_letras.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" faz parte da palavra')
    else:
        print(f'ERROU.\nA letra "{letra}" nao faz parte da palavra')
        lista_letras.pop()
        chances -= 1

    temp = ''

    for letra_secreta in secreto:
        if letra_secreta in lista_letras:
            temp += letra_secreta
        else:
            temp += '*'

    if temp == secreto:
        print('Parebens, voce ganhou.\n'
              f'a palavra era "{temp}"')
        break
    else:
        print(temp)
        print(f'Chances: {chances}')
