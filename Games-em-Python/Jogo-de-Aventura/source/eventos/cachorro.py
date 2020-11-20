import emoji
import time
import pygame


def Cachorro():
    decisão = ''
    mordidas = 0
    while decisão != 'FUGIR' and mordidas < 3:
        decisão = str(input('Digite fugir para fugir do cachorro: ')).upper()
        time.sleep(1)
        print()
        time.sleep(1)
        if(decisão == 'FUGIR'):
            time.sleep(1)
            print('Você fugiu do cachorro!')
            time.sleep(1)
        else:
            time.sleep(1)
            print(emoji.emojize('O cachorro te mordeu!' +
                                ' :dog: ' * 10, use_aliases=True))
            time.sleep(1)
            pygame.mixer.music.load('library/sounds/eventos/latida.mp3')
            pygame.mixer.music.play()
            time.sleep(6)
            mordidas += 1
            if(mordidas > 3):
                print(emoji.emojize('Fim de jogo! :bomb:', use_aliases=True))
    pass
