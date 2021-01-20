from time import sleep
from emoji import emojize
from pygame import mixer

def Seletor():
    print()
    sleep(1)
    print(emojize('Bem vindo a nossa Locadora! :camera: ', use_aliases=True))
    sleep(1)
    print('Estes são os generos que disponibilizamos para você:')
    sleep(2)
    print('Ação')
    sleep(1)
    print('Comédia')
    sleep(1)
    print('Drama')
    sleep(1)
    print('Romance')
    sleep(1)
    print('Terror')
    sleep(1)
    print()
    while True:
        sleep(1)
        escolha = str(input('Informe qual categoria deseja: ')).strip().upper()[0]
        sleep(2)
        print()
        while escolha not in 'ACDT':
            sleep(1)
            print('Digite ao menos a primeira letra do gênero, não consigo entender o que quer.')
    pass