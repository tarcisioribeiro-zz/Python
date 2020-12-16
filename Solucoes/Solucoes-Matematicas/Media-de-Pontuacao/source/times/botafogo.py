import emoji
import time
import pygame


def Botafogo():
    time.sleep(1)
    pygame.mixer.music.load('library/sounds/times/botafogo.mp3')
    pygame.mixer.music.play()
    time.sleep(17)
    print(emoji.emojize('Fogão!!!' + ' :fire: ' * 3, use_aliases=True))
    time.sleep(1)
    print()
    pass
