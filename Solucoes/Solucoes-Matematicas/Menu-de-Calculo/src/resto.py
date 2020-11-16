from time import sleep


def Resto():
    n1 = int(input('Informe um número: '))
    sleep(1)
    print()
    sleep(1)
    n2 = int(input('Informe um segundo número: '))
    sleep(1)
    print()
    sleep(1)
    print('O resto da divisão entre {} e {} é igual a {}.'.format(n1, n2, (n1 % n2)))
    sleep(1)
    print()
    pass
