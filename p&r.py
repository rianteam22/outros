"""
Sistema de perguntas e respostas com dicionários em Python
"""

print('\n\t-Questionario sobre o 2-\n')

perguntas = {
    'Pergunta 1': {
        'pergunta': '2+2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': '2*2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b',
    },
    'Pergunta 3': {
        'pergunta': '2^2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': '2/2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': '2-2?',
        'respostas': {'a': '1', 'b': '4', 'c': '0'},
        'resposta_certa': 'c',
    },
}
acertos = 0
for perg_key, perg_val in perguntas.items():
    print(f'{perg_key}: {perg_val["pergunta"]}')

    for res_key, res_val in perg_val['respostas'].items():
        print(f'\t[{res_key}]: {res_val}')

    res_us = input('Resposta: ')
    if res_us == perg_val['resposta_certa']:
        print('C')
        acertos += 1
    else:
        print('E')
    print()
qtd_per = len(perguntas)
print(f'Voce acertou {acertos/qtd_per*100:.0f}% das perguntas.')
