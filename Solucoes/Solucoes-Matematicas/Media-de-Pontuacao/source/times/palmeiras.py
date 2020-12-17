import emoji
import time
import pygame


def Fluminense():
    time.sleep(1)
    pygame.mixer.music.load('library/sounds/times/fluminense.mp3')
    pygame.mixer.music.play()
    time.sleep(16)
    print(emoji.emojize('Porco!!!' + ' :pig: ' * 3,use_aliases=True))
    time.sleep(1)
    print()
    pass
