from time import sleep
import emoji
from pygame import mixer


def Floresta():
    print()
    print(emoji.emojize('Fase da floresta ' +
                        (':evergreen_tree:' * 5), use_aliases=True))
    print()
    mixer.init()
    mixer.music.load('library/sounds/fases/floresta.mp3')
    mixer.music.play(36)
    sleep(1)
    for i in range(11, 1, -1):
        print(emoji.emojize(':evergreen_tree:' +
                            ('_' * i) + ':red_car:', use_aliases=True))
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
            print(emoji.emojize(':red_car:' + '_' * i +
                                ':evergreen_tree:', use_aliases=True))
            sleep(1)
        print()
    else:
        print(emoji.emojize(':boom:' * 5, use_aliases=True))
        print()
    pass
