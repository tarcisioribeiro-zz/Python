import emoji
import time
import pygame


def Caminhão():
    decisão = ''
    while decisão != 'DESVIAR':
        decisão = str(
            input('Digite desviar para desviar do caminhão: ')).upper()
        time.sleep(1)
        print()
        time.sleep(1)
        if(decisão == 'DESVIAR'):
            time.sleep(1)
            print('Você desviou do caminhão!')
            time.sleep(1)
        else:
            time.sleep(1)
            print(emoji.emojize('O caminhão te atropelou!' +
                                ' :truck: ' * 10, use_aliases=True))
            time.sleep(1)
            pygame.mixer.music.load('library/sounds/eventos/batida.mp3')
            pygame.mixer.music.play()
            time.sleep(5)
            print()
            time.sleep(1)
            print('Fim de jogo!')
    pass
