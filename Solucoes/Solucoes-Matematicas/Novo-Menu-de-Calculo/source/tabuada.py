from time import sleep


def calcular_tabuada(_numero):
    numero = int(_numero)
    if(numero <= 0):
        print('Informe um número inteiro entre 1 e 9.')
    if(numero >= 10):
        print('Informe um número inteiro entre 1 e 9.')
    if(numero >= 1 and numero <= 9):
        for i in range(1, 10):
            print(i, '*', numero, '=', i*numero)
            sleep(1)


numero_escolhido = int(input('Informe o número: '))
print()
enviar_tabuada = calcular_tabuada(numero_escolhido)
