num1 = int(input("Escolha o primeiro numero: "))
op = str(input('Escolha a operacao (+, -, *, /): '))
num2 = int(input('Escolha o segundo numero: '))

if op == '+':
    print(num1, '+', num2, '=', num1 + num2)
elif op == '-':
    print(num1, '-', num2, '=', num1 - num2)
elif op == '*':
    print(num1, '*', num2, '=', num1 * num2)
elif op == '/':
    print(num1, '/', num2, '=', num1 / num2)
else:
    print('Operador invalido')
