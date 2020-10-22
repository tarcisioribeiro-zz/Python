import pygame
from time import sleep
import emoji
print()
print(emoji.emojize('Bem vindo ao jogo do carrinho! :red_car:', use_aliases=True))
print()
escolha = ''
fase = int(input(emoji.emojize(
    'Qual fase deseja jogar? \n\n[ 1 ] Fase da floresta :evergreen_tree:\n[ 2 ] Fase da praia :palm_tree:\n[ 3 ] Fase do deserto :cactus:\n\nDigite aqui sua opção: ', use_aliases=True)))
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
    escolha = str(input('Desvie! o carrinho vai bater! Escreva desviar!\n\nEscreve aqui: '))
    sleep(1)
    print()
    if(escolha == 'desviar'):
        print(emoji.emojize('Ufa! o Carrinho desviou! \n\n:red_car:_:evergreen_tree:', use_aliases=True))
        print()
    else:
        print(emoji.emojize(':boom::boom::boom::boom::boom:', use_aliases=True))
        print()
if(fase == 2):
    print()
    print(emoji.emojize('Fase da praia :palm_tree::palm_tree::palm_tree::palm_tree::palm_tree:', use_aliases=True))
    print()
if(fase == 3):
    print()
    print(emoji.emojize('Fase do deserto :cactus::cactus::cactus::cactus::cactus:',use_aliases=True))
    print()