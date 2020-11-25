import time
import emoji
import pygame


def Ladrão():

    time.sleep(1)
    print()
    print(emoji.emojize('Te roubei! :gun:', use_aliases=True))
    pygame.mixer.music.load('library/sounds/eventos/roubo.mp3')
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.load('library/sounds/decisões/jogo_perdido.mp3')
    pygame.mixer.music.play()
    time.sleep(7)
    print()
    pass
