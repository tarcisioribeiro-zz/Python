print()
print('Opções da calculadora: 1 - Soma; 2 - Subtração; 3 - Multiplicação; 4 - Divisão. ')
print('Para desligar a calculadora, aperte 0.')
print()
opc = -1
n1 = 0
n2 = 0
while opc != 0:
    opc = int(input('Informe o que deseja fazer: '))
    print()
    if(opc == 1):
        n1 = int(input('Informe o primeiro número: '))
        n2 = int(input('Informe o segundo número: '))
        print()
        print('Resultado: {} + {} = {}.'.format(n1, n2, (n1 + n2)))
        print()
    if(opc == 2):
        n1 = int(input('Informe o primeiro número: '))
        n2 = int(input('Informe o segundo número: '))
        print()
        print('Resultado: {} + {} = {}.'.format(n1, n2, (n1 - n2)))
        print()
    if(opc == 1):
        n1 = int(input('Informe o primeiro número: '))
        n2 = int(input('Informe o segundo número: '))
        print()
        print('Resultado: {} + {} = {}.'.format(n1, n2, (n1 * n2)))
        print()