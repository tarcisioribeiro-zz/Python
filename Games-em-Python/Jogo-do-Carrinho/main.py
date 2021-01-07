import pygame
from time import sleep
import emoji
print()
print(emoji.emojize('Bem vindo ao jogo do carrinho! :red_car:', use_aliases=True))
print()
fase = int(input(emoji.emojize(
    'Qual fase deseja jogar? \n\n[ 1 ] Fase da floresta :evergreen_tree:\n[ 2 ] Fase da praia :palm_tree:\n[ 3 ] Fase do deserto :cactus:\n\nDigite aqui sua opção: ', use_aliases=True)))
print()
if(fase == 2):
    print()
    print(emoji.emojize('Fase da praia ' + (':palm_tree:' * 5), use_aliases=True))
    print()
    for i in range(11, 1, -1):
        print(emoji.emojize(':palm_tree:' + ('_' * i) +
                            ':red_car:', use_aliases=True))
        sleep(1)
    print()
    escolha = str(
        input('Desvie! o carrinho vai bater! Escreva desviar!!!\n\nEscreve aqui: '))
    sleep(1)
    print()
    if(escolha == 'desviar'):
        print(emoji.emojize('Ufa! o Carrinho desviou!'))
        print()
        sleep(1)
        for i in range(1, 6):
            print(emoji.emojize(':red_car:' + '_' *
                                i + ':palm_tree:', use_aliases=True))
            sleep(1)
        print()
    else:
        print(emoji.emojize(':boom::boom::boom::boom::boom:', use_aliases=True))
        print()
if(fase == 3):
    print()
    print(emoji.emojize('Fase do deserto ' + (':cactus:' * 5), use_aliases=True))
    print()
    for i in range(11, 1, -1):
        print(emoji.emojize(':cactus:' + ('_' * i) + ':red_car:', use_aliases=True))
        sleep(1)
    print()
    escolha = str(
        input('Desvie! o carrinho vai bater! Escreva desviar!!!\n\nEscreve aqui: '))
    sleep(1)
    print()
    if(escolha == 'desviar'):
        print(emoji.emojize('Ufa! o Carrinho desviou!'))
        print()
        sleep(1)
        for i in range(1, 6):
            print(emoji.emojize(':red_car:' + '_' *
                                i + ':cactus:', use_aliases=True))
            sleep(1)
        print()
    else:
        print(emoji.emojize(':boom::boom::boom::boom::boom:', use_aliases=True))
        print()
