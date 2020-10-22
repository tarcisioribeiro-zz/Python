import pygame
import time
import emoji
print()
print(emoji.emojize('Bem vindo ao jogo do carrinho! :red_car:', use_aliases=True))
print()
fase = int(input(emoji.emojize(
    'Qual fase deseja jogar? \n\n[ 1 ] Fase da floresta :evergreen_tree:\n[ 2 ] Fase da praia :palm_tree:\n[ 3 ] Fase do deserto :cactus:\n\nDigite aqui sua opção: ', use_aliases=True)))
print()
if(fase == 1):
    print(emoji.emojize('Fase da floresta :evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree:', use_aliases=True))
print()
if(fase == 2):
    print(emoji.emojize('Fase da praia :palm_tree::palm_tree::palm_tree::palm_tree::palm_tree:', use_aliases=True))
print()
if(fase == 3):
    print(emoji.emojize('Fase do deserto :cactus::cactus::cactus::cactus::cactus:',use_aliases=True))
print()