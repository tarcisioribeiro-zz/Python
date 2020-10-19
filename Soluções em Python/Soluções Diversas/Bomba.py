from time import sleep
import emoji
import time
import random
print()
print(emoji.emojize('Desarme a bomba! :bomb:', use_aliases=True))
print()
fios = ['Amarelo', 'Azul', 'Vermelho']
escolha = str(input(emoji.emojize('Qual fio você vai cortar?\n\nAmarelo\nAzul\nVermelho\n\nCorra! Digite aqui o nome da cor do fio: ', use_aliases=True)))
print()
if escolha == 'Azul':
    print('Ufa! Você desarmou a bomba.')
else:
    for i in range(11, 0, -1):
        print('{}!'.format(i))
        sleep(1)
    print()
    print(emoji.emojize(':boom: :boom: :boom: :boom: :boom:', use_aliases=True))
print()