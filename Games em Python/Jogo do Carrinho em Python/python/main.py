import pygame
from time import sleep
import emoji
print()
print(emoji.emojize('Bem vindo ao jogo do carrinho! :red_car:', use_aliases=True))
print()
fase = int(input(emoji.emojize(
        'Qual fase deseja jogar? \n\n[ 1 ] Fase da floresta :evergreen_tree:\n[ 2 ] Fase da praia :palm_tree:\n[ 3 ] Fase do deserto :cactus:\n\nDigite aqui sua opção: ', use_aliases=True)))
print()
if(fase == 1):
    print()
    print(emoji.emojize('Fase da floresta :evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree:', use_aliases=True))
    print()
    print(emoji.emojize(':evergreen_tree:__________:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':evergreen_tree:_________:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':evergreen_tree:________:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':evergreen_tree:_______:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':evergreen_tree:______:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':evergreen_tree:_____:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':evergreen_tree:____:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':evergreen_tree:___:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':evergreen_tree:__:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':evergreen_tree:_:red_car:', use_aliases=True))
    sleep(1)
    escolha = str(input('Desvie! o carrinho vai bater! Escreva desviar!!!\n\nEscreve aqui: '))
    sleep(1)
    print()
    if(escolha == 'desviar'):
        print(emoji.emojize('Ufa! o Carrinho desviou! \n\n:red_car:_:evergreen_tree:', use_aliases=True))
        sleep(1)
        print(emoji.emojize(':red_car:__:evergreen_tree:', use_aliases=True))
        sleep(1)
        print(emoji.emojize(':red_car:___:evergreen_tree:', use_aliases=True))
        sleep(1)
        print(emoji.emojize(':red_car:____:evergreen_tree:', use_aliases=True))
        sleep(1)
        print(emoji.emojize(':red_car:_____:evergreen_tree:', use_aliases=True))
        sleep(1)
        print()
    else:
        print(emoji.emojize(' :boom::boom::boom::boom::boom: ', use_aliases=True))
        print()
if(fase == 2):
    print()
    print(emoji.emojize('Fase da praia :palm_tree::palm_tree::palm_tree::palm_tree::palm_tree:', use_aliases=True))
    print()
    print(emoji.emojize(':palm_tree:__________:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':palm_tree:_________:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':palm_tree:________:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':palm_tree:_______:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':palm_tree:______:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':palm_tree:_____:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':palm_tree:____:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':palm_tree:___:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':palm_tree:__:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':palm_tree:_:red_car:', use_aliases=True))
    sleep(1)
    escolha = str(input('Desvie! o carrinho vai bater! Escreva desviar!\n\nEscreve aqui: '))
    sleep(1)
    print()
    if(escolha == 'desviar'):
        print(emoji.emojize('Ufa! o Carrinho desviou! \n\n:red_car:_:palm_tree:', use_aliases=True))
        sleep(1)
        print(emoji.emojize(':red_car:__:palm_tree:', use_aliases=True))
        sleep(1)
        print(emoji.emojize(':red_car:___:palm_tree:', use_aliases=True))
        sleep(1)
        print(emoji.emojize(':red_car:____:palm_tree:', use_aliases=True))
        sleep(1)
        print(emoji.emojize(':red_car:_____:palm_tree:', use_aliases=True))
        sleep(1)
        print()
    else:
        print(emoji.emojize(':boom::boom::boom::boom::boom:', use_aliases=True))
        print()
if(fase == 3):
    print()
    print(emoji.emojize('Fase do deserto :cactus::cactus::cactus::cactus::cactus:',use_aliases=True))
    print()
    print(emoji.emojize(':cactus:__________:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':cactus:_________:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':cactus:________:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':cactus:_______:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':cactus:______:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':cactus:_____:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':cactus:____:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':cactus:___:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':cactus:__:red_car:', use_aliases=True))
    sleep(1)
    print(emoji.emojize(':cactus:_:red_car:', use_aliases=True))
    sleep(1)
    escolha = str(input('Desvie! o carrinho vai bater! Escreva desviar!\n\nEscreve aqui: '))
    sleep(1)
    print()
    if(escolha == 'desviar'):
        print(emoji.emojize('Ufa! o Carrinho desviou! \n\n:red_car:_:cactus:', use_aliases=True))
        sleep(1)
        print(emoji.emojize(':red_car:__:cactus:', use_aliases=True))
        sleep(1)
        print(emoji.emojize(':red_car:___:cactus:', use_aliases=True))
        sleep(1)
        print(emoji.emojize(':red_car:____:cactus:', use_aliases=True))
        sleep(1)
        print(emoji.emojize(':red_car:_____:cactus:', use_aliases=True))
        sleep(1)
        print()
    else:
        print(emoji.emojize(':boom::boom::boom::boom::boom:', use_aliases=True))
        print()
else:
    print('Opção inválida. Jogo encerrado.')
    print()
    