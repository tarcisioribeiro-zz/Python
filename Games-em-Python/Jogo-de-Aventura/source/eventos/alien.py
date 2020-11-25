import time
import emoji
import pygame

def Alien():
    decisão = ''
    tentativas = 0
    while decisão != 'ESCONDER' and tentativas < 3:
        time.sleep(1)
        decisão = str(input('Digite esconder para se esconder: ')).upper()
        time.sleep(1)
        print()
        if(decisão == 'ESCONDER'):
            print('Você fugiu do Alien!')
            time.sleep(1)
        elif(decisão != 'ESCONDER'):
            time.sleep(1)
            print(emoji.emojize(' :alien: ' * 20, use_aliases=True))
            time.sleep(1)
            pygame.mixer.music.load('library/sounds/eventos/alien_chegada.mp3')
            pygame.mixer.music.play()
            time.sleep(3)
            print()
            tentativas += 1
            if(tentativas == 3):        
                time.sleep(1)
                print('O Alien te pegou!')
                time.sleep(1)
                pygame.mixer.music.load('library/sounds/eventos/alien_saída.mp3')
                pygame.mixer.music.play()
                time.sleep(3)
                pygame.mixer.music.load('library/sounds/decisões/jogo_perdido.mp3')
                pygame.mixer.music.play()
                time.sleep(7)
                print()
    pass