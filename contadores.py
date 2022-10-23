"""
for/while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
cont2 = 10

for cont1 in range(9):
    print(f'cont1 = {cont1}     cont2 = {cont2}')
    cont1 += 1
    cont2 -= 1
print('\n')
for p, r in enumerate(range(10, 1, -1)):
    print(f'progressivo = {p}     regressivo = {r}')

