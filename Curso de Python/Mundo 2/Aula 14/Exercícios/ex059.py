from time import sleep
print()
opcao = 0
n1 = int(input('Informe um primeiro número: '))
print()
n2 = int(input('Informe um segundo número: '))
print()
while (opcao != 5):
    print()
    opcao = int(input('Escolha uma opção: \n\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior dos dois números\n[ 4 ] Entre com novos números\n[ 5 ] Sair do programa\n\nDigite aqui a sua opção: '))
    sleep(1)
    print()
    if(opcao == 1):
        print('A soma de {} e {} é igual a {}.'.format(n1, n2, (n1 + n2)))
        sleep(1)
    elif(opcao == 2):
        print('A multiplicacção entre {} e {} é igual a {}.'.format(n1, n2, (n1 * n2)))
        sleep(1)
    elif(opcao == 3):
        if(n1 > n2):
            print('O maior número ente {} e {} é {}.'.format(n1, n2, n1))
            sleep(1)
        else:
            print('O maior número ente {} e {} é {}.'.format(n1, n2, n2))
            sleep(1)
    elif(opcao == 4):
        n1 = int(input('Informe um primeiro número: '))
        print()
        n2 = int(input('Informe um segundo número: '))
        print()
    elif(opcao == 5):
        print('Finalizando o programa...')
        sleep(1)
        print('Programa finalizado.')
    else:
        print('Não entendi seu comando. Tente novamente.')
print()
