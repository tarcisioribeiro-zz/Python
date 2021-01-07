import pygame
from time import sleep
import emoji
print()
print(emoji.emojize('Bem vindo ao jogo do carrinho! :red_car:', use_aliases=True))
print()
fase = int(input(emoji.emojize(
    'Qual fase deseja jogar? \n\n[ 1 ] Fase da floresta :evergreen_tree:\n[ 2 ] Fase da praia :palm_tree:\n[ 3 ] Fase do deserto :cactus:\n\nDigite aqui sua opção: ', use_aliases=True)))
print()

if(fase == 3):
    
